# Generated by Django 3.2.7 on 2021-11-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_assignment_assignment_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment_lesson_id',
            new_name='Comment_object_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_reply',
            new_name='Comment_reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_object_is',
            field=models.TextField(null=True),
        ),
    ]
