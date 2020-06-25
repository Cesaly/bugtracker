from django.urls import path
from bugtrackerapp import views

urlpatterns = [
    path('', views.index),
    path('info/<int:id>/', views.info),
    path('adduser/', views.register),
    path('addticket/', views.addticket),
    path('login/', views.login),
    path('logout/', views.logout_view),
    path('inprogress/<int:id>/', views.inprogress),
    path('invalid/<int:id>/', views.invalid),
    path('finished/<int:id>/', views.finished),
    path('edit/<int:id>/', views.editticket),
    path('authorsview/<int:id>/', views.authorsview),
    path('authorslist/', views.authorslist)
]