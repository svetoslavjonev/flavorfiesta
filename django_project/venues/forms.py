from django import forms

from django_project.venues.models import Venue


class VenueForm(forms.ModelForm):
	image = forms.ImageField()

	class Meta:
		model = Venue
		fields = '__all__'