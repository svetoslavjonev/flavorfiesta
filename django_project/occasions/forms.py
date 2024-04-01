import datetime
from dateutil.relativedelta import relativedelta

from django import forms
from django_project.occasions.models import Occasion, Seat

class OccasionForm(forms.ModelForm):

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


class OccasionCreateForm(OccasionForm):

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

class OccasionEditForm(OccasionForm):
	pass


class MonthYearForm(forms.Form):
	month_year = forms.ChoiceField(label="")

	def __init__(self, *args, **kwargs):
		super(MonthYearForm, self).__init__(*args, **kwargs)
		choices = []
		# Adjust this range to control the number of months generated
		for i in range(12):
			date = datetime.datetime.now() + relativedelta(months=i)
			month_year = date.strftime('%B, %Y')
			choices.append((month_year, month_year))
		self.fields['month_year'].choices = choices
		# Set the default value to the current month and year
		self.fields['month_year'].initial = choices[0][0] if choices else None