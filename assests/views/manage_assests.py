from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Models
from assests.models import Assests

# Serializers
from assests.serializers import AddUpdateAssestsSerializers
from assests.serializers import AssestsSerializers


class AssestsView(viewsets.ModelViewSet):
    queryset = Assests.objects.filter(is_active=True)
    serializer_classes = {
        'create' : AddUpdateAssestsSerializers,
        'update' : AddUpdateAssestsSerializers,
    }
    default_serializer_class = AssestsSerializers
    lookup_field = 'id'

    def get_queryset(self):
        self.queryset = self.queryset.filter(assests_of=self.request.user)
        return super().get_queryset()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


    # Create Custom delete to soft delete the Profile
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
        return Response({'message':'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)