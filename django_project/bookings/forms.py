from django import forms
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django_project.occasions.models import Occasion, Seat
from django_project.tickets.models import Ticket
from django_project.bookings.models import Booking


class BookingForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.occasion = kwargs.pop('occasion')
		super(BookingForm, self).__init__(*args, **kwargs)

		tickets = Ticket.objects.filter(occasion=self.occasion)
		for ticket in tickets:
			self.fields[f'tickets_{ticket.ticket_type}'] = forms.IntegerField(
				label=f'{ticket.ticket_type} Tickets',
				min_value=0,
				initial=0
			)

	def clean(self):
		cleaned_data = super().clean()
		total_tickets = sum(cleaned_data.get(f'tickets_{ticket.ticket_type}', 0) for ticket in Ticket.objects.filter(occasion=self.occasion))

		if total_tickets <= 0:
			raise forms.ValidationError("You must book at least one ticket.")
		return cleaned_data

@receiver(post_delete, sender=Booking)
def release_seats(sender, instance, **kwargs):
	"""Release seats on booking deletion."""
	occasion = instance.occasion
	reserved_seats = instance.reserved_seats.split(', ')
	for seat_number in reserved_seats:
		Seat.objects.filter(
			occasion=occasion,
			seat_number=seat_number,
			is_booked=True
		).update(is_booked=False)