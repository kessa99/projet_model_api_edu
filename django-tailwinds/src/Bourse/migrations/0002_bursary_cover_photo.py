# Generated by Django 4.2.7 on 2023-11-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bursary',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]