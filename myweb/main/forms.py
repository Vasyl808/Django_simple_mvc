from .models import Article
from django.forms import ModelForm, TextInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "intro", "text"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input title'
            }),
            "intro": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input intro'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input article'
            })
        }
