from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import BlogPost
from .forms  import BlogPostForm

def blog_post_detail_view(request, slug):
  try:
    obj = BlogPost.objects.get(slug=slug)
  except:
    raise Http404('Blog post does not exist.')

  t_name = 'blog/detail.html'
  context = {'object': obj}

  return render(request, t_name, context)

def blog_post_create_view(request):
  form = BlogPostForm(request.POST or None)

  if form.is_valid():
    print(form.cleaned_data)
    form = BlogPostForm()
  
  t_name = 'blog/create.html'
  context = {'form': form}

  return render(request, t_name, context)