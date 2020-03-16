from django.urls import path, re_path

# views
from .views import (
  blog_post_detail_view,
  blog_post_create_view
)

urlpatterns = [
  path('<str:slug>', blog_post_detail_view),
]
