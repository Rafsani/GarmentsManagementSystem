from django.db import models

class Garment(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20,null=True)


class Products(models.Model):
    garment = models.ForeignKey(Garment,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=20)
    price = models.fields.PositiveIntegerField()
    description = models.CharField(max_length=200)



class Employee(models.Model):
    Name = models.CharField(max_length=20)
    department = models.CharField(max_length=15)
    salary = models.PositiveIntegerField()
    Phone = models.CharField(max_length=12,null=True)
    address = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length= 20,null=True)


class Order(models.Model):
    CustomerName = models.CharField(max_length=20)
    CustomerPhn = models.CharField(max_length=12)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    TotalPrice = models.BigIntegerField()


