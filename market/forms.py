from django import forms
from django.db import models
from django.contrib.auth.models import User
class UserForm(forms.Form):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    solde = models.IntegerField(default=0) 
    parain = models.IntegerField(default=0)
    phone = models.CharField(max_length=10)