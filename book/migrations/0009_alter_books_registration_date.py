# Generated by Django 4.0.5 on 2022-07-02 23:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_books_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]