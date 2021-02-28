from django.contrib import admin
from .models import post
# Register your models here.
class postAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status", 'title')
    search_fields = ['title', 'content']
    prepopulated_field = {'sulg': ('title',)}

admin.site.register(post, postAdmin)