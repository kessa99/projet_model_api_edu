from django.db import models
from .choices import EXAM_CHOICES, AFRICAN_COUNTRIES, SUBJECT_CHOICES

# Create your models here.

class Archive(models.Model):
    titre = models.CharField(max_length=255)
    niveau_etude = models.CharField(max_length=255)
    filiere = models.CharField(max_length=255)
    matiere = models.CharField(max_length=255, choices=SUBJECT_CHOICES)
    author = models.CharField(max_length=255)
    date_depot = models.DateTimeField(auto_now_add=True, editable=False)
    contry = models.CharField(max_length=255, choices=AFRICAN_COUNTRIES)
    description = models.TextField(default='', blank=True, null=True)

    # Champs pour le téléchargement du sujet (uniquement pour les utilisateurs connectés)
    # Stocke le chemin du fichier dans le répertoire 'archives/'
    fichier = models.FileField(upload_to='archives/')
    type_examen = models.CharField(max_length=4, choices=EXAM_CHOICES)

    def __str__(self):
        # Retourne le titre du sujet d'examen comme représentation de l'objet dans l'administration
        return f'{self.titre}'

class Meta:
    # Trie les sujets d'examen par date de dépôt décroissante par défaut
    ordering = ['-date_depot']