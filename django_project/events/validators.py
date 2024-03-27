from django.core.exceptions import ValidationError

def validate_image_size_less_than_500kb(image):
	max_size_kb = 500
	if image.size > max_size_kb * 1024:
		raise ValidationError(f"Image size must be less than {max_size_kb}KB")