from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main ,name='main'),
    path('logout', views.logout, name='logout'),
    path('forgotpass/<str:id>', views.forgotpass, name='forgotpass'),
    path('forgot', views.forgot, name='forgot'),
    path('forgotpass/changepassword/<str:id>', views.changepassword, name='changepassword'),

    path('signup', views.signup,name='signup'),
    path('login', views.login, name='login'),
]