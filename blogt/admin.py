from django.contrib import admin
from .models import Post

# Creating the view on the Admin Interface
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')


# Register your models here.
admin.site.register(Post, PostAdmin)
