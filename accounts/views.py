from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from . import serializer

CustomUser = get_user_model()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializer.CustomUserRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_object(self):
        return self.request.user