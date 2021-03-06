from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q

# Create your models here.

user_model = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
  def published(self):
    now = timezone.now() 
    return self.filter(publish_date__lte=now)

  def search(self, query):
    lookup =  (
              Q(title__icontains=query) |
              Q(content__icontains=query) |
              Q(slug__icontains=query) |
              Q(user__first_name__icontains=query) |
              Q(user__last_name__icontains=query) |
              Q(user__last_name__icontains=query) |
              Q(user__username__icontains=query)
    )

    return self.filter(lookup)

class BlogPostManager(models.Manager):
  def get_queryset(self):
    return BlogPostQuerySet(self.model, using=self._db)

  def published(self):
    return self.get_queryset.published()

  def search(self, query=None):
    if query is None:
      return self.get_queryset().none()
    
    return self.get_queryset().published().search(query)

class BlogPost(models.Model):
  user = models.ForeignKey(user_model,
    null=True, default=1, on_delete=models.SET_NULL)
  title = models.TextField()
  slug = models.SlugField(unique=True)
  content = models.TextField(null=True, blank=True)
  publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to='image/', blank=True, null=True)

  objects = BlogPostManager()


  class Meta:
    ordering = ['-publish_date', '-updated', '-timestamp']
    
  def __str__(self):
    return str(self.title)

  def get_absolute_url(self):
    return f'/blog/{self.slug}'

  def get_edit_url(self):
    return f'/blog/{self.slug}/edit'

  def get_delete_url(self):
    return f'/blog/{self.slug}/delete'
  
  @property
  def short_content(self):
    return self.content if len(self.content) < 100 else (self.content[:97] + '...')

  def save(self, *args, **kwargs):
    self.slug = self.title.lower().replace(' ', '-')
    super().save(*args, **kwargs)

class BlogPostComment(models.Model):
  post = models.ForeignKey(BlogPost, null=True, on_delete=models.SET_NULL, related_name='comments')
  user = models.ForeignKey(user_model, null=True, on_delete=models.SET_NULL)
  content = models.CharField(max_length=220, null=False, blank=False)
  timestamp = models.DateTimeField(auto_now_add=True)

  @property
  def short_content(self):
    return self.content if len(self.content) < 100 else (self.content[:97] + '...')
