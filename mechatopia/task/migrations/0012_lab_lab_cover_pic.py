# Generated by Django 3.2.7 on 2021-11-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_rename_lab_img_lab_lab_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='Lab_cover_pic',
            field=models.TextField(null=True),
        ),
    ]
