# Generated by Django 3.1.3 on 2020-12-05 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20201205_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='user_name',
        ),
    ]
