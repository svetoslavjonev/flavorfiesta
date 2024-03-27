from django import forms

from django_project.chefs.models import Chef


class ChefForm(forms.ModelForm):
	image = forms.ImageField()

	class Meta:
		model = Chef
		fields = '__all__'