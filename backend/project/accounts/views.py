from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, UserExtensionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

@api_view(['GET','POST'])
def user_viewset(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET','POST'])
def user_contacts_viewset(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_extension = user.extension
    serializer = UserExtensionSerializer(user_extension)
    return Response(serializer.data)