from django.contrib import admin

from .models import Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner')
    list_filter = ('title',)
