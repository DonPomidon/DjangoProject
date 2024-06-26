# Generated by Django 5.0.6 on 2024-06-12 08:03

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_category_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', related_query_name='books', to='pages.category'),
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='pages.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, unique_for_date='publication_date'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique_for_month='created_at'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='books',
            field=models.ManyToManyField(related_name='publishers', related_query_name='publishers', to='pages.book'),
        ),
    ]
