# Generated by Django 5.0.6 on 2024-06-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='books',
        ),
        migrations.AddField(
            model_name='publisher',
            name='books',
            field=models.ManyToManyField(null=True, related_name='publisher', related_query_name='publishers', to='pages.book'),
        ),
    ]