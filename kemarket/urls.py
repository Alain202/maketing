"""likemarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from market import views
app_name = 'market'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('user_registration/id=<int:id>', views.user_registration, name="user_registration"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('trainer_registration', views.trainer_registration, name="trainer_registration"),
    path('learn_as_trainer', views.learn_as_trainer, name="learn_as_trainer"),
    path('reseaux', views.reseaux, name='reseaux'),
    path('retrait', views.retrait, name='retrait'),
    path('activ', views.activ, name='activ'),
    path('compte', views.compte, name='compte'),
    path('confirm', views.confirm, name="confirm"),
    path('gestion', views.gestion, name="gestion"),
    path('encour', views.encour, name="encour"),
    path('echec', views.echec, name="echec"),

]
