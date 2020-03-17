from django import forms

from .models import BlogPost

class BlogPostForm(forms.Form):
  title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
  #slug = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}))
  content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}))

  def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get('title')
    qs = BlogPost.objects.filter(title__iexact=title)

    if qs.exists():
      raise forms.ValidationError('This title has already been used.')

    return title
