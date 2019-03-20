from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(models.Model):
    id_card = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    lastname1 = models.CharField(max_length=25)
    lastname2 = models.CharField(max_length=25)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    @property
    def customer_fullname(self):
        return " ".join([self.name, self.lastname1, self.lastname2])

    @property
    def username(self):
        return self.user.username.lower()


class Plan(models.Model):
    # Internet speed will be measured in Megabits per second (mbs)
    description = models.CharField(max_length=150)
    price = models.PositiveIntegerField(default=0)
    i_speed = models.PositiveSmallIntegerField(default=0)

    @property
    def plan_speed(self):
        return str(self.i_speed) +' MBS'



class Contract(models.Model):
    id_contract = models.PositiveIntegerField(primary_key=True, default=0)
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    STATUS_CHOICES = (
        (0, 'INACTIVE'),
        (1, 'ACTIVE')

    )

    status = models.SmallIntegerField(choices=STATUS_CHOICES)


class Payment(models.Model):
    payment_date = models.DateField(auto_now_add=True)
    cc_number = models.CharField(max_length=20, default=0)
    exp_date = models.CharField(max_length=4)
    cvc = models.CharField(max_length=3,default=0)
    amount = models.PositiveIntegerField(default=0)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
