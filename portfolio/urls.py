"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib import admin

from portfolio.views import *

app_name = 'portfolio'
name = "home"

urlpatterns = [
                  path('', views.home_page_view, name=''),
                  path('home/', views.home_page_view, name='home'),
                  path('sobre/', views.sobre_page_view, name='sobre'),
                  path('contacto/', views.contacto_page_view, name='contacto'),
                  path('licenciatura/', views.licenciatura_page_view, name='licenciatura'),
                  path('blog/', views.blog_page_view, name='blog'),
                  path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
                  path('programacao/', views.programacao_page_view, name='programacao'),
                  path('virtualizacao/', views.virtualizacao_page_view, name='virtualizacao'),
                  path('reverse/', views.reverse_page_view, name='reverse'),
                  path('login/', views.login_page_view, name='login'),
                  path('logout/', views.logoutPage, name='logout'),
                  path('register/', views.registerPage, name='register'),
                  path('quizz/', views.quizz_page_view, name='quizz'),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# não tendo este static em cima fez com que eu não pudesse fazer nada e tive que refazer o código todo

#para imagens
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
