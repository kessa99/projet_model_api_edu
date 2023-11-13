from django.db import models

# Dans votre fichier Python
# from customUser.models import CustomUser

from django.urls import reverse

scholarship_types = (
    ('partial', 'Partielle'),
    ('full', "Complete"),
)

class Bursary(models.Model):
    title = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    type = models.CharField(max_length=50, default='', choices=scholarship_types)
    duration = models.IntegerField()
    amount = models.IntegerField()
    total_slots = models.IntegerField(blank=True, null=True)
    available_slots = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(default='', blank=True, null=True)
    applicants = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    cover_photo = models.ImageField(blank=True, null=True)

    def str(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('bursary', kwargs={'pk': self.pk})