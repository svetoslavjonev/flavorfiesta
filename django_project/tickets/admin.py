from django.contrib import admin
from .models import Ticket

admin.site.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ['occasion', 'price', 'ticket_type', 'ticket_number']
	list_filter = ['occasion', 'ticket_type']
	search_fields = ['occasion__name', 'ticket_type', 'ticket_number']
