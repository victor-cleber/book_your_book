# Generated by Django 4.0.5 on 2022-06-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_books_data_return_alter_books_date_checkout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='books',
            name='co_author',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
