# Generated by Django 4.1.5 on 2023-06-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_remove_bloglist_addlikes_bloglist_addlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloglist',
            name='Addlikes',
        ),
        migrations.AddField(
            model_name='bloglist',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloglist',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
