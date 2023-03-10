# Generated by Django 4.1.4 on 2022-12-29 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('released_year', models.PositiveIntegerField()),
                ('actors', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=50)),
                ('budget', models.CharField(max_length=10)),
                ('review', models.TextField()),
            ],
        ),
    ]
