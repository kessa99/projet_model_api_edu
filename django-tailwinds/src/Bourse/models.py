from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    contenu = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)

class like(models.Model):
    bourse = models.ForeignKey(Bourse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Commentaire(models.Model):
    bourse = models.ForeignKey(Bourse, on_delete=models.CASCADE)
    nom = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Commentaire de {} sur {}".format(self.nom.username, self.bourse.titre)
