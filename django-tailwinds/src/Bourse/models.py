from django.db import models

# Dans votre fichier Python
# from customUser.models import CustomUser

from django.urls import reverse

scholarship_types = (
    ('partial', 'Partielle'),
    ('full', "Complete"),
)

class Bourse(models.Model):
    titre  = models.CharField(max_length=255)
    publicateur = models.CharField(max_length=255)
    categorie  = models.CharField(max_length=255)
    financement = models.CharField(max_length=50, default='', choices=scholarship_types)
    nature = models.CharField(max_length=50, choices=[('en_ligne', 'En ligne'), ('en_presentiel', 'En présentiel')])
    lieu = models.CharField(max_length=255, default='')
    niveau = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True, null=True)
    cover_photo = models.ImageField(blank=True, null=True, upload_to="images/")
    fichier_a_joindre = models.FileField(upload_to='bourse_files/')

class Postulant(models.Model):
    bourse = models.ForeignKey(Bourse, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    commentaire = models.TextField()

class Commentaire(models.Model):
    bourse = models.ForeignKey(Bourse, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    commentaire = models.TextField()