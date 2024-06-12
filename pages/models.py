from datetime import datetime
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique_for_month='created_at')
    created_at = models.DateField(default=datetime.now)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, unique_for_date='publication_date')
    publication_date = models.DateField(blank=False)
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        related_query_name='books',
    )
    rating = models.FloatField(blank=True)
    category = models.ManyToManyField(
        Category,
        related_name='books',
        related_query_name='books',
    )

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['publication_date']

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    books = models.ManyToManyField(
        Book,
        related_name='publishers',
        related_query_name='publishers',
    )

    class Meta:
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name


