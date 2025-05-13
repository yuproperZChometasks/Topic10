from django.shortcuts import render
from .models import News_post
from .forms import New_postForm

# Create your views here.


def index_news(request):
    data = {
    'caption': 'News For',
    }
    return render(request, 'dj04_forms/index_news.html', data)

def new(request):
    return render(request, 'dj04_forms/new.html')

def news(request):
# Создаём переменную для получения всех записей.
# Прописываем словарь для передачи информации в html-шаблон.
	news = News_post.objects.all()
	return render(request, 'dj04_forms/news.html', {'news': news})
	
def create_news(request):
	form = New_postForm()
	return render(request, 'dj04_forms/add_new_post.html', {'form': form})