from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=64, verbose_name='Название категории')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')

    def __str__(self):
        return

class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Основной текст')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news',
                                 verbose_name='Категория')
    update_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title