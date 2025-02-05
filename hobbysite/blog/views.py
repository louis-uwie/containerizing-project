from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from user_management.models import Profile


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    
    def handle_no_permission(self):
        return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_articles = Article.objects.filter(author=self.request.user.profile).order_by('category')
        other_articles = Article.objects.exclude(author=self.request.user.profile).order_by('category')
        context['user_articles'] = user_articles
        context['other_articles'] = other_articles
        return context

class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={'pk': self.object.pk })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        author_articles = Article.objects.filter(author=article.author).exclude(pk=article.pk)[:2]
        context['author_articles'] = author_articles
        context['form'] = self.get_form()
        context['comments'] = Comment.objects.filter(article=self.get_object()).order_by('-created_on')

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            form.instance.author = profile
            form.instance.article = self.object
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={ 'pk': self.object.pk })
    
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'blog/article_update.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={ 'pk': self.object.pk })