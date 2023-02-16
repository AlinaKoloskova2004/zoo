# Generated by Django 4.1.7 on 2023-02-15 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=32, verbose_name='Вид животного')),
                ('name', models.CharField(max_length=128, verbose_name='Имя животного')),
                ('text', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Изображение')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('change_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('likes', models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='Лайки')),
            ],
            options={
                'verbose_name': 'Животное',
                'verbose_name_plural': 'Животные',
                'ordering': ['-publish_date', '-change_date'],
            },
        ),
    ]
