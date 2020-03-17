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

  @property
  def short_content(self):
    return self.content if len(self.content) < 100 else (self.content[:97] + '...')

  def save(self, *args, **kwargs):
    self.slug = self.title.lower().replace(' ', '-')
    super().save(*args, **kwargs)
