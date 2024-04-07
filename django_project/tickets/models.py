from django.db import models
from django.core.validators import MinValueValidator
from django_project.occasions.models import Occasion
import uuid

class Ticket(models.Model):
	occasion = models.ForeignKey(
		Occasion,
		on_delete=models.CASCADE,
		related_name='tickets',
		null=False,
		blank=False,
	)
	
	price = models.DecimalField(
		max_digits=7,
		decimal_places=2,
		null=False,
		blank=False,
		validators=[MinValueValidator(0.01), ]
	)
	
	ticket_type = models.CharField(
		max_length=50,
		null=False,
		blank=False,
	) 
	
	ticket_number = models.UUIDField(
		default=uuid.uuid4,
		editable=False,
		unique=True)

	def __str__(self):
		return f"Occasion: {self.occasion.id}, Type: {self.ticket_type}, Price: {self.price}, Number: {self.ticket_number}"
