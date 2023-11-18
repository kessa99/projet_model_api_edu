import random
import string
from django.db import models
from django.utils import timezone
from datetime import time

CATEGORIE = (
    ('se', 'EVENEMT SIMPLE'),
    ('vip', 'EVENEMENT VIP'),
    ('ecole', 'EVENEMENT SCOLAIRE'),
    ('dip', 'REMISE DE DIPLOME'),
)

TYPE_EVENT = (
    ('dip', 'DIPLOME'),
    ('MEET', 'REUNION')
)

FORMAT_EVENT = (
    ('prive', 'PRIVE'),
    ('public', 'PUBLIC')
)


def generate_unique_link():
    # Génère un lien unique de 10 caractères alphanumériques
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

class Event(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='event_images/')
    description = models.TextField()
    categorie = models.CharField(max_length=255, choices=CATEGORIE, default='se')
    organisateur = models.CharField(max_length=255)
    type_event = models.CharField(max_length=255, choices=TYPE_EVENT, default='dip')  # Ajoutez vos choix ici
    format_event = models.CharField(max_length=255, choices=FORMAT_EVENT, default='prive')  # Ajoutez vos choix ici
    date_debut =  models.DateTimeField(default=timezone.datetime(1970, 1, 1, tzinfo=timezone.utc))
    date_fin =  models.DateTimeField(default=timezone.datetime(1970, 1, 1, tzinfo=timezone.utc))
    heure_debut = models.TimeField(default=time(12, 0))
    heure_fin = models.TimeField(default=time(12, 0))
    billet = models.CharField(max_length=20, choices=(('oui', 'oui'), ('non', 'non')), default='oui')
    fuseau_horaire = models.DateTimeField(default=timezone.datetime(1970, 1, 1, tzinfo=timezone.utc))
    intervenants = models.CharField(max_length=255)

class Participate(models.Model):
    participant = models.ForeignKey(Event, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()

class like(models.Model):
    pass

class commentaire(models.Model):
    pass

class partage(models.Model):
    pass
