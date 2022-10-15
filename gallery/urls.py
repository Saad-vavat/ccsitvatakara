from django.urls import path
from .import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('cat/<int:id>/', views.ReadCat, name='gallery-cat')
]