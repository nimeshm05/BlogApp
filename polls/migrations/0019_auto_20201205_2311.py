# Generated by Django 3.1.3 on 2020-12-05 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_poll_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='user',
            new_name='user_name',
        ),
    ]
