from django.db import models
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from  market import *
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    solde = models.IntegerField(default=0) 
    parain = models.IntegerField(default=0)
    phone = models.CharField(max_length=10,default=0)
    idparain = models.IntegerField()
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        employee = Employee(user=user)
        employee.save()
        post_save.connect(create_profile, sender=User)    
class Client(models.Model):
    idclient = models.IntegerField()
    nomclient = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    methoddepot = models.CharField(max_length=50,default=0)
    nomdepot = models.CharField(max_length=100,default=0)
    telephone = models.CharField( max_length=15)
    idtransfert = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de transfert")

# Create your models here.
