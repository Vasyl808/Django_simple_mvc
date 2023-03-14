# Generated by Django 4.0.5 on 2023-02-10 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('intro', models.CharField(max_length=256, verbose_name='Intro')),
                ('text', models.TextField(verbose_name='Main text')),
                ('date', models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='Date')),
            ],
        ),
    ]
