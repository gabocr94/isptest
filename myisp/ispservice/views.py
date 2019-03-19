from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

# Register customers
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomerSerializer, UserSerializer


class Register_Customer(CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        try:
            srl = self.get_serializer(data=request.data)
            if srl.is_valid():
                srl.save()
                return Response(srl.data, status=status.HTTP_201_CREATED)
            else:
                return Response('Information not valid', status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response('An error has ocurred', status=status.HTTP_400_BAD_REQUEST)

class Register_User(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):

        try:
            srl = self.get_serializer(data=request.data)
            if srl.is_valid():
                srl.save()
                return Response(srl.data, status=status.HTTP_201_CREATED)
            else:
                return Response('Information not valid', status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response('An error has ocurred creating your user.', status=status.HTTP_400_BAD_REQUEST)

