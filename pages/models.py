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
        related_name='books',
        related_query_name='book',
    )
    rating = models.FloatField(blank=True)

    def __str__(self):
        return self.title

