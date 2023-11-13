from django.urls import path
from . import views

urlpatterns = [
    path('first_page/', views.first_page, name='first_page')
]