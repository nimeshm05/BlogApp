# Generated by Django 3.1.3 on 2020-12-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201117_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Random', max_length=30),
        ),
    ]
