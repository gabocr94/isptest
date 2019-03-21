from django.shortcuts import render

# Create your views here.
def register_customer(request):
    return render(request, 'register_customer.html')

def register_user(request):
    return render(request, 'register_user.html')