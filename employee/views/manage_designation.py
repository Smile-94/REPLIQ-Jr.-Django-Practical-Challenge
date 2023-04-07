from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Models
from employee.models import DesignationInfo

# Serializers 
from employee.serializers import DesignationSerializers


class DesignationView(viewsets.ModelViewSet):
    queryset = DesignationInfo.objects.filter(is_active=True)
    serializer_class = DesignationSerializers
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
        return Response({'message':'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
