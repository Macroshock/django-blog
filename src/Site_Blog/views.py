from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):

  return render(request, 'home.html', {
    'title': 'Homepage',
    'title_header': 'Hello there...'
    })


def about_page(request):
  return render(request, 'about.html', {
    'title': 'About',
    'title_header': 'About Us'
    })


def contact_page(request):
  return render(request, 'contact.html', {
    'title': 'Contact',
    'title_header': 'Contact Information'
    })
