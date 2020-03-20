from django.urls import path

# views
from .views import (
  search_view
)

urlpatterns = [
  path('', search_view),
]
