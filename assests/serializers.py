from rest_framework import serializers

# Models
from assests.models import Assests 
from assests.models import HandedOutAssests

# Serializers
from employee.serializers import ViewEmployeeInfoSerializers

class AddUpdateAssestsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Assests
        exclude = ('assests_id',)


class AssestsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assests
        fields = '__all__'


class HandedOutAssestsListSerializers(serializers.ModelSerializer):

    class Meta:
        model = HandedOutAssests
        fields = ('handedout_to','product','issued_id','provide_at','return_at')

class AddUpdateHandedOutAssestsSerializers(serializers.ModelSerializer):

    class Meta:
        model = HandedOutAssests
        fields = ( 'handedout_by','handedout_to','product','present_condition','return_condition')

class HandedOutViewSerializers(serializers.ModelSerializer):

    class Meta:
        model = HandedOutAssests
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        data['handedout_to']=ViewEmployeeInfoSerializers(instance=instance.handedout_to).data
        data['product']=AssestsSerializers(instance=instance.product).data
        
        return data
        