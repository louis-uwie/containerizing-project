from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name='blog_articles',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        related_name='article',
        null=True,
    )
    entry = models.TextField()
    header_image = models.ImageField(upload_to='media/blog/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(self.name, args=[str(self.name)])
    
class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name='comment',
        null=True,
        blank=True,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comment',
        null=True,
        blank=True,
    )
    entry = models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.entry
