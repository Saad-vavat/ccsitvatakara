from django.urls import path
from .import views




urlpatterns = [
    path('',views.home, name='home'),
    path('qp_link/',views.qp_link, name='qp_link'),
    path('prev_qp/<int:id>',views.qp, name='prev_qp'),
    path('exam/', views.exam, name='exam')
  
]
