from django.shortcuts import render
from .models import NewsCategory, News


# Create your views here.
# Главная страница
def home_page(request):
    # Достать данные из БД
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {'news': news, 'categories': categories}

    return render(request, 'home.html', context)