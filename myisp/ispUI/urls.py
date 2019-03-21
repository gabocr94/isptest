from django.urls import path

from .views import register_customer, register_user

urlpatterns = [

    path('user/register', register_user,name='user_register'),
    path('customer/register', register_customer,name='customer_register')
]