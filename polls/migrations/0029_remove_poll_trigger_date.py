# Generated by Django 3.1.3 on 2020-12-20 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_poll_trigger_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll_trigger',
            name='date',
        ),
    ]
