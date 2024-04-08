from django.test import TestCase
from django_project.events.forms import EventCommentForm

class EventCommentFormTests(TestCase):

	def test_event_comment_form_valid_data(self):
		form_data = {'content': 'This is a test comment.'}
		form = EventCommentForm(data=form_data)
		self.assertTrue(form.is_valid())

	def test_event_comment_form_no_data(self):
		form = EventCommentForm(data={})
		self.assertFalse(form.is_valid())  
		self.assertIn('content', form.errors)  