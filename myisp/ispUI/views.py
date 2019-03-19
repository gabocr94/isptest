from django.shortcuts import render

# Create your views here.
def register_customer(request):
    return render(request, 'register.html')