from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_project.events.models import Event
from django.utils import timezone

UserModel = get_user_model()

class EventDashboardViewTests(TestCase):
	def setUp(self):
		# Create test user
		self.user = UserModel.objects.create_user(username='testuser', password='12345')
		self.url = reverse('event-dashboard')

	def test_view_uses_correct_template_logged_in(self):
		self.client.login(username='testuser', password='12345')
		response = self.client.get(self.url)
		self.assertEqual(str(response.context['user']), 'testuser')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'events/event-dashboard.html')

