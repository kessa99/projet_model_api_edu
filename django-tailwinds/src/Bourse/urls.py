from django.urls import path
from . import views

urlpatterns = [
     path('save_bourse/', views.save_bourse, name='save_bourse'),
     path('print_bourse/', views.print_bourse, name='print_bourse'),
]
