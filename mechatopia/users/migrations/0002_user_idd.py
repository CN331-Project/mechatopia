# Generated by Django 3.2.7 on 2021-11-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='idd',
            field=models.IntegerField(null=True),
        ),
    ]