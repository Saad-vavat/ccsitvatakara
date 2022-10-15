from django.urls import path
from .import views

urlpatterns = [
   path('alumni-registration/', views.alumni, name='alumni'),
   path('',views.home, name='home' )
]
