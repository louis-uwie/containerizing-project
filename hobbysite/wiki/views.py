from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article, ArticleCategory, Comment
from user_management.models import Profile



class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'wiki/articlesList.html' 
    context_object_name = 'articles' 

    def get_queryset(self):
        queryset = super().get_queryset()
        user = Profile.objects.get(user=self.request.user)
        user_articles = queryset.filter(author=user)
        other_articles = queryset.exclude(author=user)
        return {'user_articles': user_articles, 'other_articles': other_articles}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if isinstance(context['object_list'], dict):
            context['user_articles'] = context['object_list']['user_articles']
            context['other_articles'] = context['object_list']['other_articles']
        else:
            context['other_articles'] = context['object_list']
        return context



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/articleDetails.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        category = article.category
        other_articles = Article.objects.filter(category=category).exclude(id=article.id)[:2]
        context['other_articles'] = other_articles
        return context



class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki/articleCreate.html'
    fields = ['title', 'category', 'entry', 'header_image']
    success_url = reverse_lazy('wiki:article_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()
        return context

    def form_valid(self, form):
        user = self.request.user
        profile = user.profile
        form.instance.author = profile
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={'pk': self.object.pk})



class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'wiki/articleUpdate.html'
    fields = ['title', 'category', 'entry', 'header_image']
    success_url = reverse_lazy('wiki:article_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'].queryset = ArticleCategory.objects.all()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user
        return initial

    def form_valid(self, form):
        return super().form_valid(form)



class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'wiki/commentCreate.html'
    fields = ['entry']

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.article_id = self.kwargs['article_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={'pk': self.kwargs['article_id']})
