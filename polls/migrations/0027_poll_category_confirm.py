# Generated by Django 3.1.3 on 2020-12-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20201220_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='category_confirm',
            field=models.CharField(choices=[('RANDOM', 'Random'), ('SCIENCE', 'Science'), ('COMIC', 'Comic')], default='Random', max_length=50),
        ),
    ]