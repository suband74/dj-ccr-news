from django.contrib import admin
from .models import NewsTypes, News


@admin.register(NewsTypes)
class NewsTypesAdmin(admin.ModelAdmin):
    list_display = ["name", "colour"]
    search_fields = ["name", "colour"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "short_description", "new_type"]
    list_editable = ["short_description"]
    search_fields = ["title"]