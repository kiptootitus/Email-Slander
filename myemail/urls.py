from django.urls import path
from . import views

urlpatterns = [
    path('', views.mysite, name='mysite'),
]