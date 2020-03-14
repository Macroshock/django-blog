from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
  home_title = 'Hello there...'

  return render(request, 'home.html', {
    'home_title': home_title
    })


def about_page(request):
  return HttpResponse('<h1> About Us </h1>')


def contact_page(request):
  return HttpResponse('<h1> Contact </h1>')
