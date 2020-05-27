"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bugtracker import views
from bugtracker import models


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('info/<int:id>/', views.info),
    path('adduser/', views.register),
    path('addticket/', views.addticket),
    path('login/', views.login),
    path('logout/', views.logout_view),
    path('inprogress/<int:id>/', views.inprogress),
    path('invalid/<int:id>/', views.invalid),
    path('finished/<int:id>/', views.finished),
    path('editticket/<int:id>/', views.editticket),
    path('authorsview/<int:id>/', views.authorsview),
    path('authorslist/', views.authorslist)
]
