# Generated by Django 3.2.4 on 2021-06-27 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='password',
        ),
    ]
