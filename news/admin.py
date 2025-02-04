from django.contrib import admin

from news.models import Headline


@admin.register(Headline)
class HeadlineAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'url']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 20
