# Generated by Django 3.2.13 on 2022-11-21 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_genre_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='vote_average',
            field=models.FloatField(null=True),
        ),
    ]