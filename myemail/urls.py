from django.urls import path
from . import views

urlpatterns = [
    path('', views.mysite, name='mysite'),
    path("send-emails/", send_email)

]