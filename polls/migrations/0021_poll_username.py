# Generated by Django 3.1.3 on 2020-12-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_remove_poll_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='username',
            field=models.CharField(default='Add your username...', max_length=30),
        ),
    ]