from django.contrib import admin
from django_project.venues.models import Venue

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ['name', 'capacity', 'description',]
	list_filter = ['capacity', 'name',]
	ordering = ['name', 'capacity',]
	search_fields = ['name', 'description']
