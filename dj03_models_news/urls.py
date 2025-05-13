# dj03_models_news/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_news, name='news_home'),
    path('new', views.new, name='page_2'),
    path('news', views.news, name='news'),
] 



"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('breeds', views.breeds, name='breeds'),
    path('dachshund', views.dachshund, name='dachshund'),
    path('tibetan_mastiff', views.tibetan_mastiff, name='tibetan_mastiff'),
    path('chow_chow', views.chow_chow, name='chow_chow'),
    path('sharpei', views.sharpei, name='sharpei'),
]
"""