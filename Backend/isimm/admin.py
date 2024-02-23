from django.contrib import admin
from .models import Article, Club


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'author', 'is_event')
    list_filter = ('publish_date', 'author', 'is_event')
    search_fields = ('title', 'description')
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'instagram_link', 'facebook_link')
    search_fields = ('name', 'description', 'instagram_link', 'facebook_link')
