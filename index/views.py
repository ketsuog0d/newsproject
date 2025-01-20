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

def category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(news_category=category)
    context = {'category': category, 'news': news}

    return render(request, 'category.html', context)

def news_page(request, pk):
    news = News.objects.get(id=pk)
    context = {'news': news}

    return render(request, 'news.html', context)