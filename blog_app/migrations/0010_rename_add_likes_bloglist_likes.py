# Generated by Django 4.2 on 2023-05-25 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_rename_likes_bloglist_add_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloglist',
            old_name='add_likes',
            new_name='likes',
        ),
    ]
