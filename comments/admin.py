from django.contrib import admin
from .models import Comment
# Register your models here.


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display =  ['name', 'text', 'created_time']

admin.site.register(Comment, PostAdmin)
