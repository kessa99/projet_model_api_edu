from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_bourses, name='liste_bourses'),
    path('bourse/<int:bourse_id>/', views.detail_bourse, name='detail_bourse'),
    path('bourse/saisie/', views.saisie_bourse, name='saisie_bourse'),
    path('bourse/saisie_postulant/<int:bourse_id>/', views.saisie_postulant, name='saisie_postulant'),
    path('bourse/saisie_commentaire/<int:bourse_id>/', views.saisir_commentaire, name='saisie_commentaire'),
#     path('bourse/like/<int:bourse_id>/', views.like_bourse, name='like_bourse'),
    # Ajoutez d'autres routes selon vos besoins
]

