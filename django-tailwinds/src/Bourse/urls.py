from django.urls import path
from . import views

urlpatterns = [
    path('liste_bourse/', views.liste_bourse, name='liste_bourse'),
    path('liste_bourse_admin/', views.liste_bourse_admin, name='liste_bourse_admin'),
    path('liste_postulant/<int:bourse_id>/', views.liste_postulant, name='liste_postulant'),


    path('saisie_bourse/saisie/', views.saisie_bourse, name='saisie_bourse'),

    path('details_bourse/<int:bourse_id>/', views.details_bourse, name='details_bourse'),
    path('details_bourse_admin/<int:bourse_id>/', views.details_bourse_admin, name='details_bourse_admin'),

    path('modifie_bourse/<int:bourse_id>/', views.modifie_bourse, name='modifie_bourse'),
    path('supprime_bourse/<int:bourse_id>', views.supprime_bourse, name='supprime_bourse'),


    path('saisir_postulant/<int:bourse_id>/', views.saisir_postulant, name='saisir_postulant'),
    path('saisie_commentaire/<int:bourse_id>/', views.saisie_commentaire, name='saisie_commentaire'),
#     path('bourse/like/<int:bourse_id>/', views.like_bourse, name='like_bourse'),
    # Ajoutez d'autres routes selon vos besoins
]

