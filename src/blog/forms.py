from django import forms

class BlogPostForm(forms.Form):
  title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
  #slug = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}))
  content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}))