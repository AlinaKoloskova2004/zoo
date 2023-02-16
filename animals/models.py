from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Animals(models.Model):
    kind=models.CharField(max_length=32, verbose_name="Вид животного")
    name=models.CharField(max_length=128, verbose_name="Имя животного")
    text=models.TextField(blank=False, verbose_name="Описание")
    img=models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение")
    published=models.BooleanField(default=False, verbose_name="Опубликовано")
    publish_date=models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    change_date=models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    likes = models.ManyToManyField(User, related_name="liked_posts", verbose_name="Лайки")

def __str__(self):
    return self.name 
    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"
        ordering = ["-publish_date", "-change_date"]
# Create your models here.
