from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Models
from accounts.models import User
from accounts.models import Profile

# Serializers for accouts create view and update, delete
from accounts.serializers import UserListSerializers
from accounts.serializers import SignUpUserSerializer

# Serializers for profile create, update, view, delete
from accounts.serializers import ProfileListSerializer
from accounts.serializers import UpdateViewProfileSerializers

class AccountsView(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_classes = {
        'create' : SignUpUserSerializer,
        'update' : SignUpUserSerializer
    }
    default_serializer_class = UserListSerializers
    lookup_field = 'id'

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
    
    # Create Custom delete to soft delete the user
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
        return Response({'message':'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.filter(is_active=True)
    serializer_classes = {
        'create' : UpdateViewProfileSerializers,
        'update' : UpdateViewProfileSerializers,
        'retrieve' : UpdateViewProfileSerializers
    }
    default_serializer_class = ProfileListSerializer
    lookup_field = 'id'

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