from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
  #title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
  #slug = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}))
  #content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}))
  class Meta:
    model = BlogPost
    fields = ['title', 'content', 'publish_date', 'image']
    widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

  def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get('title')
    instance = self.instance
    qs = BlogPost.objects.filter(title__iexact=title)

    if instance is not None:
      qs = qs.exclude(pk=instance.pk)

    if qs.exists():
      raise forms.ValidationError('This title has already been used.')

    return title
