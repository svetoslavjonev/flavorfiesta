from django.db import models
from django.contrib.auth import get_user_model
from django_project.occasions.models import Occasion

UserModel = get_user_model()

class Booking(models.Model):
	
	occasion = models.ForeignKey(
		Occasion,
		on_delete=models.CASCADE,
		related_name='bookings',
		null=False,
		blank=False,
	)
	
	user = models.ForeignKey(
		UserModel,
		on_delete=models.CASCADE,
		related_name='bookings',
		null=True,
		blank=True,
	)
	
	booking_time = models.DateTimeField(
		auto_now_add=True
	)
	
	number_of_tickets = models.PositiveIntegerField(
		null=True,
		blank=True
	)
	
	type_of_tickets = models.TextField(
		null=True,
		blank=True,
	)
	
	total_price = models.DecimalField(
		max_digits=7,
		decimal_places=2,
		null=True,
		blank=True,
	)
	
	reserved_seats = models.TextField(
		null=True,
		blank=True,
	)
	
	is_completed = models.BooleanField(
		default=False,
		null=False,
		blank=False
	)

	def __str__(self):
		return f"{self.user.username} - {self.occasion} ({self.number_of_seats} seats, {self.status})"