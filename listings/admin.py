from django.contrib import admin
from.models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'neighborhood', 'price', 'build_type', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor', 'price', 'neighborhood', 'build_type')
  list_editable = ('is_published',)
  search_fields = ('title', 'state', 'zipcode', 'price', 'build_type')
  list_per_page = 25
admin.site.register(Listing, ListingAdmin)