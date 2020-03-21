from django import forms

from .models import BlogPost, BlogPostComment

class BlogPostForm(forms.ModelForm):

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

class BlogPostCommentForm(forms.ModelForm):

  class Meta:
    model = BlogPostComment
    fields = ['user', 'post', 'content']
    widgets = {
          'user': forms.NumberInput(attrs={'hidden': True}),
          'post': forms.NumberInput(attrs={'hidden': True}),
          'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment', 'rows': 5}),
        }
  
  def __init__(self, *args, **kwargs):
        super(BlogPostCommentForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
