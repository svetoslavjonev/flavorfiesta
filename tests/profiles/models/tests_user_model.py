from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date

UserModel = get_user_model()

class AppUserModelTests(TestCase):
	def test_user_save__with_first_name_only_letters__expect_correct_result(self):
		user = UserModel.objects.create_user(
			username="testuser",
			email="testuser@example.com",
			password="Testpass123!",
			first_name="Testname",
			last_name="Lastname",
		)
		user.full_clean()  # This will validate the model fields
		user.save()
		self.assertIsNotNone(user.pk)

	def test_user_save__with_first_name_with_numbers__expect_validation_error(self):
		user = UserModel(
			username="testuser2",
			email="testuser2@example.com",
			password="Testpass123!", 
			first_name="Testname2",  # This should cause a ValidationError
			last_name="Lastname",
		)

		with self.assertRaises(ValidationError) as ve:
			user.full_clean()
		# No need to save the user as we are testing the validation, which should fail
		self.assertIsNotNone(ve.exception)

	def test_user_creation_with_valid_birth_date(self):
		user = UserModel.objects.create_user(
			username="birthday_user",
			email="birthday@example.com",
			password="TestPass123!",
			birth_date=date(1990, 1, 1)
		)
		self.assertEqual(user.birth_date, date(1990, 1, 1))

	def test_user_full_name_property(self):
		user = UserModel.objects.create_user(
			username="full_name_user",
			email="fullname@example.com",
			password="TestPass123!",
			first_name="John",
			last_name="Doe"
		)
		self.assertEqual(user.full_name, "John Doe")

	def test_user_creation_with_invalid_email_format(self):
		with self.assertRaises(ValidationError) as ve:
			user = UserModel(
				username="bademail_user",
				email="bademail",
				password="TestPass123!"
			)
			user.full_clean()

	def test_user_creation_with_invalid_gender_choice(self):
		with self.assertRaises(ValidationError) as ve:
			user = UserModel(
				username="genderchoice_user",
				email="gender@example.com",
				password="TestPass123!",
				gender="X"  #'M', 'F', 'O' are the only valid choices
			)
			user.full_clean()