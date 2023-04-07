from rest_framework import serializers

# Import Models
from employee.models import DesignationInfo
from employee.models import EmployeeInfo


class DesignationSerializers(serializers.ModelField):

    class Meta:
        model = DesignationInfo
        fields = '__all__'