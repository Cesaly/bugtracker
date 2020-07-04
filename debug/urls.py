from django.urls import path
from debug import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('ticket/<int:id>/', views.info),
    path('adduser/', views.register),
    path('addticket/', views.addticket),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('inprogress/<int:id>/', views.inprogress),
    path('invalid/<int:id>/', views.invalid),
    path('finished/<int:id>/', views.finished),
    path('edit/<int:id>/', views.editticket),
    path('authorsview/<int:id>/', views.authorsview),
]