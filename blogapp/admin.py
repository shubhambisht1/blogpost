from django.contrib import admin
from blogapp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','created')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}

# Register your models here.
admin.site.register(Post,PostAdmin)
