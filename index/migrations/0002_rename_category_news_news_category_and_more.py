# Generated by Django 5.1.4 on 2024-12-10 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='category',
            new_name='news_category',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='news_content',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='news_title',
        ),
    ]
