from django.contrib import admin

from .models import Article, ArticleCategory, Comment

'''
Admin User
    username: uwie
    password: admintester1

    username: louisuwie
    password: admintester_mac
    
Test User
    username: louis
    password: usertester1
'''

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on')
    list_filter = ('category', 'created_on')
    search_fields = ('title', 'entry')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_on', 'updated_on')
    list_filter = ('created_on',)
    search_fields = ('author__username', 'article__title', 'entry')
