from django import forms

from django_project.tickets.models import Ticket


class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = '__all__'