from django.urls import path

from .views import Register_Customer

urlpatterns = [

    path('api/register', Register_Customer.as_view(),name='register_api')
]