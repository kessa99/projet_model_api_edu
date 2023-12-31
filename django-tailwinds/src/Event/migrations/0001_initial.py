# Generated by Django 4.2.7 on 2023-11-07 20:28

import Event.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('lieu', models.CharField(max_length=255)),
                ('organisateur', models.CharField(max_length=255)),
                ('lien_partage', models.CharField(default=Event.models.generate_unique_link, max_length=10, unique=True)),
            ],
        ),
    ]
