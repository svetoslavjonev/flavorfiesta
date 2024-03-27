from django import forms

from django_project.events.models import Event, EventComment


class EventForm(forms.ModelForm):
	image = forms.ImageField()
	
	class Meta:
		model = Event
		fields = '__all__'


class EventCommentForm(forms.ModelForm):
	class Meta:
		model = EventComment
		fields = ('content',)
		widgets = {
			'content': forms.Textarea()
		}
		
