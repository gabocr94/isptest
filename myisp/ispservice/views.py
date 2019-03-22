import stripe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

# Register customers
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.conf import settings
from stripe.error import StripeError

from ispservice.models import Customer, Plan, Contract, Payment
from .serializers import CustomerSerializer, UserSerializer, Customer_List_Srlzr, PlanSerializer, Contract_Serializer, \
    Payments_Serializer


# Customer classes
class Register_Customer(CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny,]
    http_method_names = ['post','get' ]

    def post(self, request, *args, **kwargs):

        try:
            srl = self.get_serializer(data=request.data)
            print(self.request.user)
            srl.data['email'] = self.request.user.email
            srl.data['user'] = self.request.user
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
            # logout any current user
            logout(request)

            userSrl = self.get_serializer(data=request.data)
            if userSrl.is_valid():
                new_user = User.objects.create_user(
                    username=userSrl.validated_data['username'],
                    password=userSrl.validated_data['password']
                )
                if new_user is not None:
                    login(request, new_user)
                    return Response(userSrl.data, status=status.HTTP_201_CREATED)
                else:
                    print('User not found')
                    return Response('User not found', status=status.HTTP_404_NOT_FOUND)
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


# Plans classes

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
    permission_classes = ()  # IsAuthenticated,)

    def get_queryset(self):
        plan = Plan.objects.all()
        plan = plan.filter(pk=self.pk)  # , user=self.request.user)
        return plan

    def list(self, request, *args, **kwargs):

        try:
            self.pk = kwargs['pk']
            return super(Get_Plan, self).list(request, *args, **kwargs)

        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)


# Contract Views

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


# Payments views

class Create_Payment(CreateAPIView):
    serializer_class = Payments_Serializer
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def post(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():

                print(serializer.validated_data['cvc'])
                token = stripe.Token.create(
                    card={
                        "number": serializer.validated_data['cc_number'],
                        "exp_month": serializer.validated_data['exp_date'][0:2],
                        "exp_year": serializer.validated_data['exp_date'][2:4],
                        "cvc": serializer.validated_data['cvc'],
                    },
                )

                # Save this to variable to use response from stripe
                stripe_response = stripe.Charge.create(
                    amount=serializer.validated_data['amount'],
                    currency='usd',
                    source=token,

                )

                if stripe_response:
                    serializer.validated_data['paid'] = stripe_response['paid']
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:

                    return Response('An error occurred with your payment', status=status.HTTP_400_BAD_REQUEST)

            else:
                print(serializer.errors)
                return Response('Information is not valid', status=status.HTTP_400_BAD_REQUEST)

        except StripeError as e:
            print(e)
            return Response('Your payment information is not correct', status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response('An error has occurred creating your Payment.', status=status.HTTP_400_BAD_REQUEST)


class List_All_Payments(ListAPIView):
    serializer_class = Payments_Serializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        payments = Payment.objects.all()
        return payments

    def list(self, request, *args, **kwargs):

        try:
            self.get_queryset()
            return super(List_All_Payments, self).list(request, *args, **kwargs)

        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)


class List_Customer_Payments(ListAPIView):
    serializer_class = Payments_Serializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        payments = Payment.objects.all()
        payments = payments.filter(contract_id__id_customer=self.pk, contract_id__id_customer__user=self.request.user)
        return payments

    def list(self, request, *args, **kwargs):

        try:
            print(kwargs)
            self.pk = kwargs['pk']
            self.get_queryset()
            return super(List_Customer_Payments, self).list(request, *args, **kwargs)

        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)


class Get_Payment(ListAPIView):
    serializer_class = Payments_Serializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        contract = Contract.objects.all()
        contract = contract.filter(pk=self.pk, contract_id__id_customer__user=self.request.user)
        return contract

    def list(self, request, *args, **kwargs):

        try:
            self.pk = kwargs['pk']
            return super(Get_Contract, self).list(request, *args, **kwargs)

        except Exception as e:
            print(e)
            return Response('Data not found', status=status.HTTP_404_NOT_FOUND)
