# Generated by Django 3.2.7 on 2021-11-07 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_challenge_challenge_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge_tag',
            old_name='Challenge_tag_Id',
            new_name='Challenge_tag_ID',
        ),
        migrations.RenameField(
            model_name='challenge_tag',
            old_name='Challenge_name',
            new_name='Challenge_tag_name',
        ),
    ]