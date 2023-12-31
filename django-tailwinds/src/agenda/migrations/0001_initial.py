# Generated by Django 4.2.7 on 2023-11-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.CharField(choices=[('1T', 'premier Trimestre'), ('2T', 'deuxieme Trimestre'), ('3T', 'troisieme trimestre'), ('BAC', 'Baccalauréat'), ('PROB', 'Probatoire'), ('UNIV', 'Université')], max_length=50)),
                ('notes', models.CharField(max_length=255)),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
            ],
        ),
    ]
