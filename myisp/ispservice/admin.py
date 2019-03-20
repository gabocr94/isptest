from django.contrib import admin

# Register your models here.
from ispservice.models import Plan, Customer, Payment, Contract

admin.site.register(Plan)
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Contract)
