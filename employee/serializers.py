from rest_framework import serializers

# Import Models
from employee.models import DesignationInfo
from employee.models import EmployeeInfo


class DesignationSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = DesignationInfo
        fields = '__all__'

class EmployeeInfoListSerializers(serializers.ModelSerializer):

    class Meta:
        model = EmployeeInfo
        fields = ('full_name','position','joining_date','employee_id')

class AddUpdateEmployeeInfoSerializers(serializers.ModelSerializer):

    class Meta:
        model = EmployeeInfo
        fields = ('employee_of','full_name','position','phone','national_id','photo','signature')


class ViewEmployeeInfoSerializers(serializers.ModelSerializer):

    class Meta:
        model = EmployeeInfo
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        data['position']=DesignationSerializers(instance=instance.position).data
        
        return data