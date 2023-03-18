from unicodedata import name
from django.urls import path
from . import views

app_name = "subscription_app"

urlpatterns =[
    path('homepage/',views.home_page , name = "homepage"),
    path('register/', views.register, name = "register"),
    path('login/', views.login_page, name= 'login'),
    path("select/<int:id>/",views.select_page, name = 'select'),
    path("confirm_payment/",views.confirm_payment, name = 'confirm'),
]