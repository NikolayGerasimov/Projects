# Generated by Django 4.2 on 2023-08-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director_email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
        ),
    ]
