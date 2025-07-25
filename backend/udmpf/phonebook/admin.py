from django.contrib import admin

from .models import Department, Kontakt, Subdivision


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Kontakt)
class KontaktAdmin(admin.ModelAdmin):
    search_fields = (
        'name', 's_name', 'last_name', 'ip_number',
        'phone_number', 'e_mail',
    )
    list_display = (
        'last_name', 'name', 's_name', 'ip_number',
        'phone_number',
        'e_mail', 'department', 'subdivision'
    )
