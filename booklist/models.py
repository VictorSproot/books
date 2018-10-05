from django.db import models

CATEGORIES = (
    (1, 'Русский'),
    (2, 'Английский')
)


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    description = models.TextField(blank=True, db_index=True, verbose_name='Описание')
    desc_for_find = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')
    category = models.ManyToManyField('Category', related_name='books', verbose_name='Категория')
    lang_category = models.IntegerField(choices=CATEGORIES, default=1, db_index=True, verbose_name='Язык')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
