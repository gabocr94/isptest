from django.urls import path

from .views import Register_Customer, Register_User, List_Customers, Get_Customer, List_Plans, Get_Plan, \
    Create_Contract, List_Contracts, Get_Contract, Create_Payment, List_All_Payments, List_Customer_Payments, \
    Get_Payment

urlpatterns = [

    path('api/create/customer', Register_Customer.as_view(), name='customer_api'),
    path('api/create/user', Register_User.as_view(), name='user_api'),
    path('api/list/customers', List_Customers.as_view(), name='customer_list'),
    path('api/details/customer/<int:pk>', Get_Customer.as_view(), name='customer_details'),
    path('api/list/plans', List_Plans.as_view(), name='plan_list'),
    path('api/details/plan/<int:pk>', Get_Plan.as_view(), name='plan_details'),
    path('api/create/contract', Create_Contract.as_view(), name='contract_api'),
    path('api/list/contracts', List_Contracts.as_view(), name='customer_list'),
    path('api/details/contract/<int:pk>', Get_Contract.as_view(), name='contract_details'),
    path('api/create/payment', Create_Payment.as_view(), name='payment_api'),
    path('api/details/payment/<int:pk>', Get_Payment.as_view(), name='contract_details'),
    path('api/list/payments', List_All_Payments.as_view(), name='payments_list'),
    path('api/list/mypayments/<int:pk>', List_Customer_Payments.as_view(), name='my_payments_list'),

]
