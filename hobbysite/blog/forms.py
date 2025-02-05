from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
    
        disabled_fields = ['author']
        for field_name in disabled_fields:
            self.fields[field_name].disabled = True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
    
        disabled_fields = ['author','article']
        for field_name in disabled_fields:
            self.fields[field_name].disabled = True

