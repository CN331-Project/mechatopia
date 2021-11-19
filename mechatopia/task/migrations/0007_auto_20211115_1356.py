# Generated by Django 3.2.7 on 2021-11-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20211107_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge_in_tag',
            fields=[
                ('Challenge_in_tag_Id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Challenge_id', models.IntegerField(null=True)),
                ('Challenge_tag_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lab_in_tag',
            fields=[
                ('Lab_in_tag_Id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Lab_id', models.IntegerField(null=True)),
                ('Lab_tag_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='Challenge_tag_id',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='Lab_tag_id',
        ),
    ]
