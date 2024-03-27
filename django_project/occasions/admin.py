from django.contrib import admin

from django_project.occasions.models import Occasion, Seat

@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
	list_display = ('event', 'venue', 'chef', 'start_time', 'end_time')
	list_filter = ('event', 'venue', 'chef', 'start_time')
	search_fields = ('event__name', 'venue__name', 'chef__name')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
	list_display = ('occasion', 'seat_number', 'is_booked')
	list_filter = ('occasion', 'is_booked')
	search_fields = ('occasion__event__name', 'seat_number')
	ordering = ('occasion', 'seat_number')
