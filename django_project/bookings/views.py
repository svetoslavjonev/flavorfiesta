from django.contrib import messages
from django.db import transaction
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth import mixins as auth_mixin
from django_project.bookings.models import Booking
from django_project.bookings.forms import BookingForm
from django_project.occasions.models import Occasion, Seat
from django_project.tickets.models import Ticket


class BookingView(auth_mixin.LoginRequiredMixin, views.View):

	login_url = "/profiles/singup-user/"
	
	def get_context_data(self, **kwargs):
		context = {}
		occasion_id = kwargs.get('occasion_id')  # Assumes 'occasion_id' is captured from the URL
		occasion = get_object_or_404(Occasion, pk=occasion_id)
		tickets = Ticket.objects.filter(occasion=occasion)
		available_seats_count = Seat.objects.filter(occasion=occasion, is_booked=False).count()

		context.update({
			'occasion': occasion,
			'tickets': tickets,
			'available_seats_count': available_seats_count
		})

		if 'form' not in context:
			context['form'] = BookingForm(occasion=occasion)

		return context

	def get(self, request, occasion_id, *args, **kwargs):
		context = self.get_context_data(occasion_id=occasion_id)
		return render(request, 'bookings/book-occasion.html', context)

	def post(self, request, occasion_id, *args, **kwargs):
		occasion = get_object_or_404(Occasion, pk=occasion_id)
		form = BookingForm(request.POST, occasion=occasion)

		if form.is_valid():
			tickets_data = form.cleaned_data
			total_price = 0
			reserved_seats = []

			try:
				with transaction.atomic():
					# Check for available seats and raise ValidationError if needed
					for ticket in Ticket.objects.filter(occasion=occasion):
						ticket_count = tickets_data.get(f'tickets_{ticket.ticket_type}', 0)
						available_seats = Seat.objects.filter(occasion=occasion, is_booked=False)[:ticket_count]

						if available_seats.count() < ticket_count:
							# If not enough seats, add a non-field error and break the loop
							form.add_error(None, "Not enough available seats for one or more ticket types.")
							raise forms.ValidationError("Not enough available seats.")

						# If enough seats, proceed with booking logic
						for seat in available_seats:
							seat.is_booked = True
							seat.save()
							reserved_seats.append(str(seat.seat_number))
							total_price += ticket.price

					# Only proceed with creating the booking if no ValidationError has been raised
					booking = Booking.objects.create(
						occasion=occasion,
						user=request.user,
						total_price=total_price,
						reserved_seats=', '.join(reserved_seats),
						number_of_tickets=sum(tickets_data.values()),
						is_completed=True
					)

					messages.success(request, "Your booking has been successfully completed.")
					return redirect('booking-details', pk=booking.pk)  # Adjust as needed

			except forms.ValidationError:
				# If not enough seats or any other validation error, the form will be re-rendered with errors
				pass

		context = self.get_context_data(occasion_id=occasion_id)
		context['form'] = form  # Include the form with errors in the context
		return render(request, 'bookings/book-occasion.html', context)

class BookingDetailView(auth_mixin.LoginRequiredMixin, views.DetailView):
	login_url = "/profiles/singup-user/"
	model = Booking
	context_object_name = 'booking'
	template_name = 'bookings/booking-details.html'

	def get_queryset(self):
		"""Ensure a user can only access their own bookings."""
		queryset = super().get_queryset()
		return queryset.filter(user=self.request.user)