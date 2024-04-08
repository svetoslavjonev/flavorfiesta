from django.test import TestCase
from django.contrib.auth import get_user_model
from django_project.profiles.forms import UserCreateForm, ProfileEditForm

UserModel = get_user_model()

class ProfileFormTests(TestCase):

	def test_user_create_form_with_valid_data(self):
		form_data = {
			'username': 'newuser',
			'email': 'newuser@example.com',
			'password1': 'StrongPassword123',
			'password2': 'StrongPassword123'
		}
		form = UserCreateForm(data=form_data)
		self.assertTrue(form.is_valid())

	def test_user_create_form_with_invalid_data(self):
		UserModel.objects.create_user('testuser', 'testuser@example.com', 'TestPass123')
		form_data = {
			'username': 'testuser',  # Duplicate username
			'email': 'testemail@example.com',
			'password1': 'TestPass123',
			'password2': 'TestPass123'
		}
		form = UserCreateForm(data=form_data)
		self.assertFalse(form.is_valid())

	def test_profile_edit_form_with_valid_data(self):
		user = UserModel.objects.create_user('edituser', 'edituser@example.com', 'TestPass123')
		form_data = {
			'email': 'editusernewemail@example.com',
			'first_name': 'FirstName',
			'last_name': 'LastName',
			'gender': 'F'
		}
		form = ProfileEditForm(data=form_data, instance=user)
		self.assertTrue(form.is_valid())

	def test_profile_edit_form_required_fields(self):
		user = UserModel.objects.create_user('requiredfieldstest', 'requiredfieldstest@example.com', 'TestPass123')
		form_data = {
			# intentionally left blank to test required fields
		}
		form = ProfileEditForm(data=form_data, instance=user)
		
		self.assertFalse(form.is_valid())