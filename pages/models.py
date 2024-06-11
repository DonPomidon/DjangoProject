from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField(blank=False)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='book',
        related_query_name='books',
    )
    rating = models.FloatField(blank=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['publication_date']

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name
