# Generated by Django 3.1.3 on 2020-12-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_poll_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll_Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='old_values', max_length=100)),
            ],
        ),
    ]
