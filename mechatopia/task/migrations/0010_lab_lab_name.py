# Generated by Django 3.2.7 on 2021-11-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_lab_lab_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='Lab_name',
            field=models.TextField(null=True),
        ),
    ]