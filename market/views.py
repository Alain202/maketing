from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from cinetpay_sdk.s_d_k import Cinetpay
from cinetpay_sdk.s_d_k import Cinetpay
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from market.models import Employee
from market.models import Client
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
import json
from random import random
from bs4 import BeautifulSoup
import load
import requests
from django.http import JsonResponse
def home(request):
    return render(request, 'home.html', locals())
def compte(request):
    return render(request,'compte.html')   
def reseaux(request):
    return render(request, 'reseau.html')
def retrait(request):
    return render(request, 'retrait.html')  
def activ(request):
    return render(request, 'activ.html')      
 
def user_registration(request,id):
    us = User.objects.get(id=id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')

        last_name = request.POST.get("last_name")
        user_name = request.POST.get("user_name")
        email= request.POST.get("email")
        solde = 0
        parain = 0
        idparain = us.id
        mobile= request.POST.get("mobile")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
    
        if password1 == password2:
            if User.objects.filter(username = user_name).exists():

                messages.info(request,'Username Taken')

                return redirect('user_registration')

            elif User.objects.filter(email = email).exists():

                messages.info(request,'Email Taken')

                return redirect('user_registration')

            else:
                 
                user = User.objects.create_user(first_name= first_name,last_name = last_name, username = user_name, email = email, password = password1 )
                
                user.save()
                e= Employee(user=user,phone= mobile, solde=solde, parain= parain, idparain=idparain )
                e.save()
                pr = us.employee.solde
                pr = pr + 100
                us.employee.solde = pr
                us.employee.parain = us.employee.parain + 1
                us.employee.save()
                print('User Created')
                print(first_name)
                return redirect('login')

        else:
            print("password not matching...")
            return redirect('user_registration')
            return redirect('/')
    else:
        return render(request, 'user_registration.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        user = auth.authenticate(username = user_name, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def trainer_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get("last_name")
        user_name = request.POST.get("user_name")
        email= request.POST.get("email")
        mobile= request.POST.get("mobile")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('trainer_registration')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Taken')
                return redirect('trainer_registration')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = user_name, email = email, password = password1)
                user.is_staff=True
                user.save()
                trainer_registration = TrainerRegistration.objects.create(user=user, status = False)
                return redirect('login')
        else:
            print("password not matching...")
            return redirect('trainer_registration')
        return redirect('/')
    else:
        return render(request, 'trainer_registration.html')
'lms/trainer_registration.html'
def learn_as_trainer(request):
    user = request.user
    trainer_registration = TrainerRegistration.objects.create(user= user, status = False)
    user_info = User.objects.filter(username = user.username)
    for info in user_info:
        if info.username:
            user.is_staff=True
            user.save()
    return render(request, 'learn_as_trainer.html')
# Create your views here.

def edit_user(request, id):
# querying the User object with pk from url
    user = User.objects.get(id=id)
    if request.method=='POST':
        e= Employee(user=user)
        e.save()
        phone= request.POST.get('mobile')
        solde = 0
        parain = 0
        user.employee.phone = phone
        user.employee.solde = solde 
        user.employee.parain = parain
    

    return render(request, "edit_user.html", {"noodle": id,})
def confirm(request):
    if request.method == 'POST':
        idclient = request.POST.get("idclient")
        telephone = request.POST.get("telephone")
        nom = request.POST.get("last_name")
        idtransfert = request.POST.get("transfert")
        prenom = request.POST.get("first_name")
        methoddepot = request.POST.get("methoddepot")
        nomdepot =  request.POST.get("namedepot")

        client = Client.objects.all()
        for cl in client:
            if cl.idtransfert == idtransfert:
                print('cette id de transaction existe deja dans la base de donnees')
                return redirect('echec')
           
        client = Client(idclient=idclient,methoddepot=methoddepot,nomdepot=nomdepot, telephone=telephone,nomclient=nom, idtransfert=idtransfert, prenom=prenom)
        client.save()
                
        return redirect('encour')
    else:
        print("erreur veiller recommencer")    
    return render(request,'confirm.html')  
def encour(request):
    return render(request,'encour.html')
def echec(request):
    return render(request,'echec.html')
def gestion(request):
    if request.method == 'POST':
        passs = request.POST.get("passs")
        if passs == "Alain2020":
            user = User.objects.all()
            client = Client.objects.all()
            for us in user:   
                for cl in client:
                    if cl.idclient == us.id:
                        us.employee.solde = us.employee.solde + 1000
                        us.employee.save()
                        for ks in user:
                            if ks.id == us.employee.idparain:
                                ks.employee.solde = ks.employee.solde + 200
                                ks.employee.save()
                        cl.delete()
                             
                        
            return redirect('/')            
        else:
            print("vous aver pas acces a  cette section")  
    return render(request,'gestion.html')                      


# Create your views here.
