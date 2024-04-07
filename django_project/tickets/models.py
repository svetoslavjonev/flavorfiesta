from django.db import models
from django.core.validators import MinValueValidator
from django_project.occasions.models import Occasion

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

	def __str__(self):
		return f"Occasion: {self.occasion}, Type: {self.ticket_type}, Price: {self.price}"
