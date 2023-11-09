from django.db import models

# Create your models here.
CLASSES_CHOICES = (
    ('1T', 'premier Trimestre'),
    ('2T', 'deuxieme Trimestre'),
    ('3T', 'troisieme trimestre'),
    ('BAC', 'Baccalauréat'),
    ('PROB', 'Probatoire'),
    ('UNIV', 'Université'),
)


class Agenda(models.Model):
    niveau = models.CharField(max_length=50, choices=CLASSES_CHOICES)
    notes =  models.CharField(max_length=255)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()