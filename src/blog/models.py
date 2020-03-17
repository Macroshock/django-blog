from django.conf import settings
from django.db import models

# Create your models here.

user_model = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
  user = models.ForeignKey(user_model, 
    null=True, default=1, on_delete=models.SET_NULL)
  title = models.TextField()
  slug = models.SlugField(unique=True)
  content = models.TextField(null=True, blank=True)
