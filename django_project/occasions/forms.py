from django import forms
from django_project.occasions.models import Occasion, Seat


class OccasionCreateForm(forms.ModelForm):
	
	class Meta:
		model = Occasion
		fields = '__all__' 
		widgets = {
			'start_time': forms.DateTimeInput(attrs={
				'type': 'datetime-local',
				'placeholder': 'DD-MM-YYYY HH:MM',
			}),
			'end_time': forms.DateTimeInput(attrs={
				'type': 'datetime-local',
				'placeholder': 'DD-MM-YYYY HH:MM',
			}),
		}

	def save(self, commit=True):
		occasion = super().save(commit=commit)
		venue_capacity = occasion.venue.capacity
		objs = []

		for seat_number in range(1, venue_capacity + 1):
			objs.append(Seat(seat_number=str(seat_number), occasion=occasion, is_booked=False))

		Seat.objects.bulk_create(objs)

		if commit:
			occasion.save()

		return occasion
