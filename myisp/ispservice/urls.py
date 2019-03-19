from django.urls import path

from .views import Register_Customer, Register_User

urlpatterns = [

    path('api/customer', Register_Customer.as_view(),name='customer_api'),
    path('api/user', Register_User.as_view(),name='user_api')
]