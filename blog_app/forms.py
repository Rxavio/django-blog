from django.forms import ModelForm
from .models import *
from django import forms


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here!!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('body',)
