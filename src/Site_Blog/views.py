from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):

  return render(request, 'home.html', {
    'title': 'Homepage',
    'title_header': 'Hello there...'
    })


def about_page(request):
  return HttpResponse('<h1> About Us </h1>')


def contact_page(request):
  return HttpResponse('<h1> Contact </h1>')
