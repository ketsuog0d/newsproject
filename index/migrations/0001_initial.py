# Generated by Django 5.1.4 on 2024-12-06 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64, verbose_name='Название категории')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Основной текст')),
                ('update_data', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='index.newscategory', verbose_name='Категория')),
            ],
        ),
    ]