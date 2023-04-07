from rest_framework import serializers

# Models
from accounts.models import User
from accounts.models import Profile 


# User list and details seralizers
class UserListSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','is_staff','is_clients')


# User Creation and Update Serializer
class SignUpUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password')

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        attrs['is_clients'] = True
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)
        user = User.objects.create_clients(email, password, **validated_data)
        user.set_password(password)
        user.save()
        return user

# Companty Profile List Seralizers

# Serializer to view the user email
class ProfileUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)

class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user','company_name','company_type','contact_no')

class UpdateViewProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        data['user']=ProfileUserSerializers(instance=instance.user).data
        
        return data




