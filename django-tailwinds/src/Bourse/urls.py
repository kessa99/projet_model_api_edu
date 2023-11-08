from django.urls import path
from . import views

urlpatterns = [
     path('bourse/', views.bourse, name='bourse'),
]
