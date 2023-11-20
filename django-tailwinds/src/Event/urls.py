from django.urls import path
from . import views

urlpatterns = [
   path('saisie_event/', views.saisie_event, name='saisie_event'),
   path('saisir_participant/<int:event_id>/', views.saisir_participant, name='saisir_participant'),


   path('liste_event/', views.liste_event, name='liste_event'),
   path('liste_event_admin/', views.liste_event_admin, name='liste_event_admin'),
   path('liste_participant/<int:event_id>', views.liste_participant, name='liste_participant'),

   path('detail_event/<int:event_id>/', views.detail_event, name='detail_event'),
   path('detail_event_admin/<int:event_id>/', views.detail_event_admin, name='detail_event_admin'),

   path('modifie_event/<int:event_id>/', views.modifie_event, name='modifie_event'),

   path('supprime_event/<int:event_id>/', views.supprime_event, name='supprime_event'),

] 
