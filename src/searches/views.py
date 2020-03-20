from django.shortcuts import render

from blog.models import BlogPost

from .models import SearchQuery

def search_view(request):
  q = request.GET.get('q', None)
  user = None
  if request.user.is_authenticated:
    user = request.user
  
  context = {
    'query': q
    }

  if q is not None:
    SearchQuery.objects.create(user=user, query=q)
    context['blog_list'] = BlogPost.objects.search(query=q)
  
  print(context['blog_list'])
  t_name = 'search/view.html'

  return render(request, t_name, context)
