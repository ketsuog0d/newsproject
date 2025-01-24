from django.shortcuts import render, redirect
from .models import NewsCategory, News
from .forms import RegForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


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

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()


            login(request, user)
            return redirect('/')

        context = {'form': RegForm, 'message': 'Пароль или почта неверны!'}
        return render(request, self.template_name, context)


def search(request):
    if request.method == 'POST':
        get_news = request.POST.get('search')

        if News.objects.get(news_title__iregex=get_news):
            searched_news = News.objects.get(news_title__iregex=get_news)
            return redirect(f'/news/{searched_news.id}')
        else:
            return redirect('/')