from django.shortcuts import render
from .models import News_post

# Create your views here.


def index_news(request):
    data = {
    'caption': 'News',
    }
    return render(request, 'dj03_models_news/index_news.html', data)

def new(request):
    return render(request, 'dj03_models_news/new.html')

"""
def news(request):
    return render(request, 'dj03_models_news/news.html')
"""



# Открываем файл views.py, импортируем класс.
# Создаём переменную для получения всех записей.
# Прописываем словарь для передачи информации в html-шаблон.

def news(request):
	news = News_post.objects.all()
	return render(request, 'dj03_models_news/news.html', {'news': news})

