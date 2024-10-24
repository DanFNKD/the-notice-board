from django.contrib import admin
from .models import Post, Comment, Tag, Vote
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'author', 'created_on')
    search_fields = ('title',)
    list_filter = ('status',)
    ordering = ['status', 'title']
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Vote)