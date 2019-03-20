from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

# Register customers
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from ispservice.models import Customer, Plan, Contract
from .serializers import CustomerSerializer, UserSerializer, Customer_List_Srlzr, PlanSerializer, Contract_Serializer


#Customer classes
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
            return Response('An error has occurred', status=status.HTTP_400_BAD_REQUEST)


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
            return Response('An error has occurred creating your user.', status=status.HTTP_400_BAD_REQUEST)


class List_Customers(ListAPIView):
    serializer_class = Customer_List_Srlzr
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        customers = Customer.objects.all()
        return customers

    def list(self, request, *args, **kwargs):

        try:
            self.get_queryset()
            return super(List_Customers, self).list(request, *args, **kwargs)


        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)


class Get_Customer(ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        customer = Customer.objects.all()
        customer = customer.filter(pk=self.pk, user=self.request.user)
        return customer

    def list(self, request, *args, **kwargs):

        try:
            self.pk = kwargs['pk']
            return super(Get_Customer, self).list(request, *args, **kwargs)

        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)


#Plans classes

class List_Plans(ListAPIView):
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        plans = Plan.objects.all()
        return plans

    def list(self, request, *args, **kwargs):

        try:
            self.get_queryset()
            return super(List_Plans, self).list(request, *args, **kwargs)


        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)


class Get_Plan(ListAPIView):
    serializer_class = PlanSerializer
    permission_classes = ()#IsAuthenticated,)

    def get_queryset(self):
        plan = Plan.objects.all()
        plan = plan.filter(pk=self.pk) #, user=self.request.user)
        return plan

    def list(self, request, *args, **kwargs):

        try:
            self.pk = kwargs['pk']
            return super(Get_Plan, self).list(request, *args, **kwargs)

        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)


#Contract Views

class Create_Contract(CreateAPIView):
    serializer_class = Contract_Serializer

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
            return Response('An error has occurred creating your user.', status=status.HTTP_400_BAD_REQUEST)


class List_Contracts(ListAPIView):
    serializer_class = Contract_Serializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        contracts = Contract.objects.all()
        return contracts

    def list(self, request, *args, **kwargs):

        try:
            self.get_queryset()
            return super(List_Contracts, self).list(request, *args, **kwargs)


        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)


class Get_Contract(ListAPIView):
    serializer_class = Contract_Serializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        contract = Contract.objects.all()
        contract = contract.filter(pk=self.pk, )
        return contract

    def list(self, request, *args, **kwargs):

        try:
            self.pk = kwargs['pk']
            return super(Get_Contract, self).list(request, *args, **kwargs)

        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)