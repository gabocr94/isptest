from django.db import models


# Create your models here.
class Customer(models.Model):
    id_card = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    lastname1 = models.CharField(max_length=25)
    lastname2 = models.CharField(max_length=25)
    email = models.EmailField()

    @property
    def full_name(self):
        return "%s %s %s"(self.name, self.lastname1, self.lastname2)


class Plan(models.Model):
    # Internet speed will be measured in Megabits per second (mbs)
    description = models.CharField(max_length=150)
    price = models.PositiveIntegerField(default=0)
    i_speed = models.PositiveSmallIntegerField(default=0)

    @property
    def get_speed(self):
        return "%s Mbs"(self.i_speed)


class Contract(models.Model):
    id_contract = models.CharField(max_length=30, primary_key=True)
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    STATUS_CHOICES = (
        (0, 'INACTIVE'),
        (1, 'ACTIVE')

    )

    status = models.SmallIntegerField(choices=STATUS_CHOICES)


class Payment(models.Model):
    payment_date = models.DateField(auto_now=False)
    cc_number = models.PositiveIntegerField(default=0)
    exp_date = models.CharField(max_length=4)
    amount = models.PositiveIntegerField(default=0)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
