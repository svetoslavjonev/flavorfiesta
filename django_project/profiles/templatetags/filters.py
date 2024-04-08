from django.template import Library
from django_project.occasions.models import Occasion, Seat

register = Library()


@register.filter
def placeholder(field, value):
	field.field.widget.attrs['placeholder'] = value
	return field


@register.filter
def autofocus(field):
	field.field.widget.attrs['autofocus'] = True
	return field


@register.filter
def has_available_seats(occasion):
	return Seat.objects.filter(occasion=occasion, is_booked=False).exists()