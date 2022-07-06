from django.db import models
from datetime import date
from user.models import User


class Categories(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    registration_date = models.DateField(auto_now_add=True)
    excluded_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'

    def __str__(self) -> str:
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    co_author = models.CharField(max_length=30, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    excluded_date = models.DateField(auto_now_add=True)
    member = models.CharField(max_length=100, blank=True, null=True)
    is_loan = models.BooleanField(default=False)
    date_checkout = models.DateTimeField(blank=True, null=True)
    data_return = models.DateTimeField(blank=True, null=True)
    loan_time = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Book'

    def __str__(self):
        return self.name


