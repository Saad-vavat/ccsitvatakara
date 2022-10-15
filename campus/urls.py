from django.urls import path
from .import views

urlpatterns = [
    path('campuslife/', views.campuslife, name='campuslife'),
]