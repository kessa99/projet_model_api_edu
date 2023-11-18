from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
   path('saisie_archive/', views.saisie_archive, name='saisie_archive'),

   path('liste_archive/', views.liste_archive, name='liste_archive'),
   path('liste_archive_admin/', views.liste_archive_admin, name='liste_archive_admin'),

   path('detail_archive/<int:archive_id>/', views.detail_archive, name='detail_archive'),
   path('detail_archive_admin/<int:archive_id>/', views.detail_archive_admin, name='detail_archive_admin'),

   path('modifie_archive/<int:archive_id>/', views.modifie_archive, name='modifie_archive'),

   path('supprime_archive/<int:archive_id>/', views.supprime_archive, name='supprime_archive'),
] 