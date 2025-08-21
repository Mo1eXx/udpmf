from django.contrib import admin

from .models import Department, Kontakt, Subdivision


class KontaktInline(admin.TabularInline):
    model = Kontakt
    extra = 0


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'output_order')
    inlines = (KontaktInline,)
    list_editable = ('output_order',)


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'output_order')
    inlines = (KontaktInline,)
    list_editable = ('output_order',)


@admin.register(Kontakt)
class KontaktAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display_links = ('last_name', 'name', 's_name')
    search_fields = (
        'name', 's_name', 'last_name', 'ip_number',
        'phone_number', 'e_mail', 'job_title'
    )
    list_display = (
        'last_name', 'name', 's_name', 'ip_number',
        'phone_number', 'job_title',
        'e_mail', 'output_order', 'department', 'subdivision'
    )
    list_filter = ('department', 'subdivision')
    list_editable = ('department', 'subdivision', 'output_order')

