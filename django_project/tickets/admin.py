from django.contrib import admin
from django_project.tickets.models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ['occasion', 'price', 'ticket_type']
	list_filter = ['occasion', 'ticket_type']
	search_fields = ['occasion__name', 'ticket_type']
