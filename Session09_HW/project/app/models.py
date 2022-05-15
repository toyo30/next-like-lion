from pydoc import ModuleScanner
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    content = models.TextField(default='')
    hit = models.PositiveIntegerField(default=0)
        
    def __str__(self):
        return str(self.title)

    # @property
    # def update_counter(self):
    #     self.hit = self.hit + 1
    #     self.save()