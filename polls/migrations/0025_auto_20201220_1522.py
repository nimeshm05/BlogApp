# Generated by Django 3.1.3 on 2020-12-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_poll_trigger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='category',
            field=models.CharField(choices=[('RANDOM', 'Random'), ('SCIENCE', 'Science'), ('COMIC', 'Comic')], default='Random', max_length=50),
        ),
    ]
