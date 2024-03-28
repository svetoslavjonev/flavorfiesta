from django.db import models
from django.utils.text import slugify
from django_project.events.models import Event
from django_project.chefs.models import Chef
from django_project.venues.models import Venue


class Occasion(models.Model):
	
	event = models.ForeignKey(
		Event,
		on_delete=models.CASCADE,
		related_name='occasions',
		null=False,
		blank=False,
	)
	
	venue = models.ForeignKey(
		Venue,
		on_delete=models.CASCADE,
		related_name='occasions',
		null=False,
		blank=False,
	)
	
	chef = models.ForeignKey(
		Chef,
		on_delete=models.CASCADE,
		related_name='occasions',
		null=False,
		blank=False,
	)
	
	start_time = models.DateTimeField(
		null=False,
		blank=False,
	)
	
	end_time = models.DateTimeField(
		null=False,
		blank=False,
	)
	
	slug = models.SlugField(max_length=100, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(f"{self.event.name}-{self.venue.name}-{self.start_time.strftime('%Y-%m-%d')}")
		super(Occasion, self).save(*args, **kwargs)

	def __str__(self):
		return f"{self.event.name} at {self.venue.name} on {self.start_time.strftime('%Y-%m-%d')}"

	class Meta:
		ordering = ['start_time']


class Seat(models.Model):
	
	occasion = models.ForeignKey(
		Occasion,
		on_delete=models.CASCADE,
		related_name='seats',
		null=False,
		blank=False,
	)
	
	seat_number = models.CharField(
		max_length=5,
		null=False,
		blank=False,
	)
	
	is_booked = models.BooleanField(
		default=False,
		null=False,
		blank=False,)
