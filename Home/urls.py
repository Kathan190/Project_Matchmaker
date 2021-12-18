from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="matchmaker-in"),
    path('home/', views.home, name="matchmaker-home"),
    path('contact/', views.contact, name="matchmaker-in"),
    path('about/', views.about, name="matchmaker-about"),
    path('main', views.main, name="matchmaker-main"),
    path('assignment', views.assignment, name="matchmaker-assignment"),
    path('cs', views.cs, name="matchmaker-cs"),
    path('se', views.se, name="matchmaker-se"),
    path('bm', views.bm, name="matchmaker-bm"),
]
