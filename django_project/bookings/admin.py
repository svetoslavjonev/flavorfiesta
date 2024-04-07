from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ['user', 'occasion', 'booking_time', 'number_of_tickets', 'type_of_tickets', 'total_price', 'is_completed']
	list_filter = ['occasion', 'is_completed', 'booking_time']
	search_fields = ['user__username', 'occasion__name', 'type_of_tickets']
	ordering = ['booking_time', 'user']
