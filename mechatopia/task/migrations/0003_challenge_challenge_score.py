# Generated by Django 3.2.7 on 2021-11-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20211024_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='Challenge_score',
            field=models.IntegerField(null=True),
        ),
    ]
