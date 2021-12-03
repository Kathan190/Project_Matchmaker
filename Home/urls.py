from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="matchmaker-in"),
    path('home/', views.home, name="matchmaker-home"),
    path('contact/', views.contact, name="matchmaker-in"),
    path('about/', views.about, name="matchmaker-about"),
    path('main', views.main, name="matchmaker-main"),
]
