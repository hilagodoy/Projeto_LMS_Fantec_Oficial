"""Fantec_Oficial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core.views import *


#para cada view criada, devo acrescentar a lista abaixo a função correspondente
urlpatterns = [
    path('', index),
    #diretorios de cursos
    path('cursos/', cursos),
    path('cursos/curso_adm/', curso_adm),
    path('cursos/curso_sistemas/', curso_sistemas),
    path('cursos/curso_ads/', curso_ads),
    path('cursos/curso_bd/', curso_bd),
    path('cursos/curso_engenharia/', curso_engenharia),
    path('cursos/curso_gestao/', curso_gestao),
    path('cursos/curso_jogos/', curso_jogos),
    path('cursos/curso_engenharia/', curso_engenharia),
    path('cursos/curso_producao/', curso_producao),
    path('cursos/curso_redes/', curso_redes),
    #fim diretorio cursos
    path('sobre/', sobre),
    path('contato/', contato),
    path('acesso/', acesso),
    path('admin/', admin.site.urls),
]