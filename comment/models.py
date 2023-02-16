from django.db import models
from animals.models import Animals


class Comment(models.Model):
    text = models.TextField(blank=False) 
    date_of_create = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=32)
    animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    published = models.BooleanField(default=False) 

    def __str__(self):
        return self.text [ :32] + '...'    

    class Meta:
        ordering = ('-date_of_create', )