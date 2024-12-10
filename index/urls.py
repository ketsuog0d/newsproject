from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('news/<int:pk>', views.news_page),
    path('сategory/<int:pk>', views.category_page)
]