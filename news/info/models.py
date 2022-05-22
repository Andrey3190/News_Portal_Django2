

from django.db import models
from django.core.validators import MinValueValidator


class News(models.Model):
    name = models.CharField(
        max_length=1000,
        unique=True,
    )

    data = models.DateTimeField(auto_now_add=True)


    description = models.TextField()

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',
    )



    def __str__(self):
        return f'{self.name.title()}: {self.description[:200]}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()