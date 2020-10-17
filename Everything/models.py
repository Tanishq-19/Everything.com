from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Seller(models.Model):
	seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
	fullname = models.CharField(max_length=50)
	shop = models.CharField(max_length=50)
	p_type = models.CharField(max_length=25)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	zipcode = models.CharField(max_length=10)
	contact = models.CharField(max_length=20) 

class Customer(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	zipcode = models.CharField(max_length=10)
	contact = models.CharField(max_length=20) 

class Chat(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipient")
	chat = models.CharField(max_length=500)
	takeaway = models.BooleanField(default=False)
	finish = models.BooleanField(default=False)
	total = models.IntegerField(default=0)