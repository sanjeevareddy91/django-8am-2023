# Generated by Django 4.1.4 on 2023-01-11 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0006_remove_movies_actors_movies_actors'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
