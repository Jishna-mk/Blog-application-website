# Generated by Django 4.1.5 on 2023-06-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_remove_bloglist_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloglist',
            name='likes',
        ),
        migrations.AddField(
            model_name='bloglist',
            name='Addlikes',
            field=models.IntegerField(default=0),
        ),
    ]
