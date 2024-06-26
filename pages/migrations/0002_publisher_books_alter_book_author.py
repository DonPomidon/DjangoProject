# Generated by Django 5.0.6 on 2024-06-11 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='books',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', related_query_name='publishers', to='pages.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='book', related_query_name='books', to='pages.author'),
        ),
    ]
