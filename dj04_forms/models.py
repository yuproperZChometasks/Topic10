from django.db import models

# Create your models here.

class News_post(models.Model):
	title = models.CharField('Название новости', max_length=150)
	short_description = models.CharField('Краткое описание новости', max_length=200)
	text = models.TextField('Новость')
	pub_date = models.DateTimeField('Дата публикации')
	posted_news_name = models.CharField('Выложил новость', max_length=200)

	
	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
