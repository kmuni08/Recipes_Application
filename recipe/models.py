from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('recipe:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category, related_name='recipe', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Recipes'
        ordering = ('-created',)


    def get_absolute_url(self):
        return reverse('recipe:recipe_detail', args=[self.slug])


    def __str__(self):
        return self.title
