# Generated by Django 3.2.6 on 2022-01-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_comment_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='Lesson_body',
            field=models.TextField(null=True),
        ),
    ]