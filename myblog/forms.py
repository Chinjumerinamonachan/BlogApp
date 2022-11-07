from django import forms
from myblog.models import Article,Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","slug","author", "image", "content","status"]



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')