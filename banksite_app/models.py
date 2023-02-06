from django.db import models


# Create your models here.
SAVINGS_ACCOUNT = 'Savings Account'
CURRENT_ACCOUNT = 'Current Account'

ACCOUNT_CHOICES = [
    (SAVINGS_ACCOUNT,SAVINGS_ACCOUNT),
    (CURRENT_ACCOUNT,CURRENT_ACCOUNT)
]

class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    dob = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    mailid = models.EmailField(max_length=100)
    address = models.TextField(max_length=500)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    ac_type = models.CharField(max_length=100, choices=ACCOUNT_CHOICES)
    materials = models.CharField(max_length=100)

    def __str__(self):
        return self.name
