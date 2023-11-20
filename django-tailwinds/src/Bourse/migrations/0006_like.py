# Generated by Django 4.2.7 on 2023-11-20 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bourse', '0005_rename_commentaire_commentaire_contenu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bourse.bourse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
