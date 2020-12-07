# Generated by Django 3.1.3 on 2020-12-05 17:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0011_auto_20201205_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='username',
        ),
        migrations.AddField(
            model_name='poll',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
