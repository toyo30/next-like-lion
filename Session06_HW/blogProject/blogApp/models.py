from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.TextField(null=True, default='')
    date = models.TextField(null=True, default='')

    def __str__(self):
        return self.title

