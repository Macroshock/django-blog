from django.contrib import admin

# Register your models here.
from .models import BlogPost, BlogPostComment

class BlogPostAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug', 'user', 'short_content']
  search_fields = ['title']

class BlogPostCommentAdmin(admin.ModelAdmin):
  list_display = ['user', 'post', 'short_content']

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPostComment, BlogPostCommentAdmin)
