from django.urls import path
from . import views

urlpatterns = [
    path('alumni/', views.result, name='result')
]