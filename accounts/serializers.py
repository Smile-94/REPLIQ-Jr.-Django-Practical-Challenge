from rest_framework import serializers

# Models
from accounts.models import User
from accounts.models import Profile 



class UserListSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','is_staff','is_clients')


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