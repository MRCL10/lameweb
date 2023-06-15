from django.urls import path
from Mywebsite import views

urlpatterns = [
    path('', views.home)
]