# Generated by Django 4.0.5 on 2022-07-06 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_books_category_books_excluded_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category'},
        ),
    ]