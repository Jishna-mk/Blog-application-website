# Generated by Django 4.2 on 2023-05-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_alter_bloglist_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglist',
            name='Blog_category',
            field=models.CharField(blank=True, choices=[('option1', 'Business'), ('option2', 'Culture'), ('option3', 'Food'), ('option4', 'Technology'), ('option4', 'Social')], default='option4', max_length=500, null=True),
        ),
    ]