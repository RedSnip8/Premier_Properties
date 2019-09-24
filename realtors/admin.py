from django.contrib import admin
from.models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date', 'is_mvp')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    search_fields = ('id', 'name')
    list_per_page = 10


admin.site.register(Realtor, RealtorAdmin)