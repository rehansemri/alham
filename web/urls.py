
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('contact/',views.contact , name="contact"),
    path('about/',views.about , name="about"),
    path('process/',views.process , name="process"),
    path('manufactor/',views.manufactor , name="manufactor"),
]
