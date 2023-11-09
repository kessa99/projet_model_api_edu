import random
import string
from django.db import models


def generate_unique_link():
    # Génère un lien unique de 10 caractères alphanumériques
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

class Event(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    organisateur = models.CharField(max_length=255)
    lien_partage = models.CharField(max_length=10, unique=True, default=generate_unique_link)

    def __str__(self):
        return f'{self.nom}'