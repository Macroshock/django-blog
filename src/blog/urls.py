from django.urls import path, re_path

# views
from .views import (
  blog_post_detail_page
)

urlpatterns = [
    path('<str:slug>', blog_post_detail_page)
]
