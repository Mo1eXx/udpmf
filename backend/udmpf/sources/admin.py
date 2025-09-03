from django.contrib import admin

from .models import Source


class SourcesInline(admin.TabularInline):
    model = Source
    extra = 0


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner')
    list_filter = ('owner',)
