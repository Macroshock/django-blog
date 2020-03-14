from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import BlogPost

def blog_post_detail_page(request, slug):
  try:
    obj = BlogPost.objects.get(slug=slug)
  except:
    raise Http404('Blog post does not exist.')

  t_name = 'blog_post_detail.html'
  context = {'object': obj}

  return render(request, t_name, context)

