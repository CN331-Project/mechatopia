# Generated by Django 3.2.7 on 2021-11-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_rename_lesson_group_admin_id_lesson_group_lesson_group_admin_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='Lesson_pic',
            field=models.TextField(null=True),
        ),
    ]