from django.contrib import admin
from .models import Article, ArticleCategory, Comment

class ArticleInline(admin.TabularInline):
    model = Article

class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

class ArticleCategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)