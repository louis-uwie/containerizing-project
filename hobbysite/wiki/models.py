from django.db import models
from django.conf import settings
from django.utils import timezone

from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='articles'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    header_image = models.ImageField(upload_to='media/wiki', blank=True, null=True)
    author = models.ForeignKey(
        Profile, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='wiki_articles'
    )

    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(
        Profile, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="wiki_comments"
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.article.title}"
