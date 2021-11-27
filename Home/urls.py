from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="matchmaker-home"),
    path('about/', views.about, name="matchmaker-about")
]
