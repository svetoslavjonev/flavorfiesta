from django.core.exceptions import ValidationError


def validate_name_has_only_letters(value):
	for char in value:
		if not char.isalpha():
			raise ValidationError("Name must contain only letters.")