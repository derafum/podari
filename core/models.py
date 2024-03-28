from django.db import models


class Customers(models.Model):
    login = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role_id = models.IntegerField()


class Status(models.Model):
    name = models.TextField(max_length=100)


class Orders(models.Model):
    date = models.DateField(auto_now_add=True)
    customer_id = models.IntegerField()
    status_id = models.IntegerField()


class Type(models.Model):
    name = models.TextField(max_length=100)


class Gift(models.Model):
    title = models.TextField(max_length=100)
    price = models.FloatField(max_length=3)
    description = models.TextField(max_length=255)
    image = models.ImageField(verbose_name=None, height_field=None, width_field=None, max_length=100)
    type_id = models.IntegerField()


class Sale(models.Model):
    gift_id = models.IntegerField()
    order_id = models.IntegerField()
    amount = models.IntegerField()