# Generated by Django 3.2.8 on 2021-10-10 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_auto_20211011_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
    ]