from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
