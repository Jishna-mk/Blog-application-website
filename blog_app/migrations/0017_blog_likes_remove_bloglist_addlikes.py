# Generated by Django 4.1.5 on 2023-06-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0016_remove_bloglist_dislikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_likes',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('Addlikes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='bloglist',
            name='Addlikes',
        ),
    ]
