from django.db import models


class CostEntry(models.Model):
    date = models.DateField()
    cost_for = models.CharField(max_length=100)
    cost_group = models.CharField(max_length=100, choices=(
        ('Food', 'Food'),
        ('Clothes', 'Clothes'),
        ('Housing', 'Housing'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Entertainment & Welfare', 'Entertainment & Welfare'),
        ('Transportation', 'Transportation'),
    ))
    price = models.DecimalField(max_digits=10, decimal_places=2)
