# Generated by Django 3.1.3 on 2020-12-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20201205_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='username',
            field=models.CharField(default='Add your username', max_length=30),
        ),
    ]
