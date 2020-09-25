from django.db import models
from products.models import Category


class Question(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, blank=False)
    dateandtime = models.DateTimeField(auto_now_add=True, blank=False)
    description = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.title


