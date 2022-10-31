from django import forms
from myblog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","slug","author", "image", "content","status"]