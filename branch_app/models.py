from django.db import models


# Create your models here.
class Ernakulam(models.Model):
    branch_name = models.CharField(max_length=100)
    branchid = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    hours = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name


class Trivandrum(models.Model):
    branch_name = models.CharField(max_length=100)
    branchid = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    hours = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name


class Kollam(models.Model):
    branch_name = models.CharField(max_length=100)
    branchid = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    hours = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name


class Kottayam(models.Model):
    branch_name = models.CharField(max_length=100)
    branchid = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    hours = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name


class Thrissur(models.Model):
    branch_name = models.CharField(max_length=100)
    branchid = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    hours = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name

