from django.urls import path

from placement.models import placement
from .import views

urlpatterns = [
    path('placement/', views.Placement, name= 'placement' )
]