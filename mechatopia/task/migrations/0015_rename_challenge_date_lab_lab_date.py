# Generated by Django 3.2.7 on 2021-11-21 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_lab_challenge_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lab',
            old_name='Challenge_date',
            new_name='Lab_date',
        ),
    ]
