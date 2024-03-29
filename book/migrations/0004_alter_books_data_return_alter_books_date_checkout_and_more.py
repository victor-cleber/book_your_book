# Generated by Django 4.0.5 on 2022-06-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_books_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='data_return',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='date_checkout',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='loan_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='member',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
