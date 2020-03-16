from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

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
  form = ContactForm(request.POST or None)
  if form.is_valid():
    form = ContactForm()
  
  t_name = 'contact.html'
  context = {
    'title': 'Contact',
    'title_header': 'Contact Information',
    'form': form
    }
  
  return render(request, t_name, context)
