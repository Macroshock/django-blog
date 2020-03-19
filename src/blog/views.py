from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
from .models import BlogPost
from .forms  import BlogPostForm

def blog_post_detail_view(request, slug):
  try:
    obj = BlogPost.objects.get(slug=slug)
  except:
    raise Http404('Blog post does not exist.')

  t_name = 'blog/detail.html'
  context = {'object': obj, 'detail': True}

  return render(request, t_name, context)

def blog_post_list_view(request):
  if request.user.is_authenticated:
    list = BlogPost.objects.filter()
  else:
    list = BlogPost.objects.filter().published()

  t_name = 'blog/list.html'
  context = {
    'title': 'Blog Posts',
    'title_header': 'List of Blog Posts',
    'list': list,
    }

  return render(request, t_name, context)

@staff_member_required
def blog_post_create_view(request):
  form = BlogPostForm(request.POST or None)

  if form.is_valid():
    form.save()
    # Reset the form
    form = BlogPostForm()
  
  t_name = 'blog/create.html'
  context = {
    'title': 'Create post',
    'title_header': 'Create new post',
    'form': form
    }

  return render(request, t_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
  try:
    obj = BlogPost.objects.get(slug=slug)
  except:
    raise Http404('Blog post does not exist.')

  form = BlogPostForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.cleaned_data['slug'] = form.cleaned_data['title'].lower().replace(' ', '-')
    print(form.cleaned_data)
    form.save()
    return redirect('/blog')

  t_name = 'blog/update.html'
  context = {
    'title': 'Update post',
    'title_header': 'Update existing post',
    'form': form,
    'object': obj
    }

  return render(request, t_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
  try:
    obj = BlogPost.objects.get(slug=slug)
  except:
    raise Http404('Blog post does not exist.')

  if request.method == 'POST':
    obj.delete()
    return redirect('/blog')

  t_name = 'blog/delete.html'
  context = {
    'title': 'Delete post',
    'title_header': 'Delete post',
    'object': obj
    }

  return render(request, t_name, context)