import django.utils.timezone
from django.db import models
from datetime import date

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    co_author = models.CharField(max_length=30, blank=True)
    registration_date = models.DateField(default= django.utils.timezone.now)
    member = models.CharField(max_length=100, blank=True, null = True)
    is_loan = models.BooleanField(default=False)
    date_checkout = models.DateTimeField(blank=True, null = True)
    data_return = models.DateTimeField(blank=True, null = True)
    loan_time = models.DateTimeField(blank=True, null = True)

    class Meta:
        verbose_name = 'Book'

    def __str__(self):
        return self.name


