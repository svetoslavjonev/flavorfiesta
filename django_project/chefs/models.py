from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django_resized import ResizedImageField
from django_project.chefs.validators import validate_image_size_less_than_500kb, validate_name_has_only_letters_and_spaces

class Chef(models.Model):

	MAX_NAME_LENGTH = 50
	MAX_BIO_LENGTH = 600
	IMAGE_SIZE = [400, 600]
	
	SPECIALTIES = (
		('french_cuisine', 'French Cuisine'),
		('italian_cuisine', 'Italian Cuisine'),
		('pastry_and_baking', 'Pastry & Baking'),
		('asian_cuisine', 'Asian Cuisine'),
		('farm_to_table', 'Farm-to-Table'),
		('molecular_gastronomy', 'Molecular Gastronomy'),
		('vegetarian_and_vegan', 'Vegetarian & Vegan'),
		('seafood', 'Seafood'),
		('bbq_and_grilling', 'BBQ and Grilling'),
		('middle_eastern_cuisine', 'Middle Eastern Cuisine'),
		('mexican_cuisine', 'Mexican Cuisine'),
		('fusion_cuisine', 'Fusion Cuisine'),
		('health_and_nutrition', 'Health and Nutrition'),
		('street_food', 'Street Food'),
	)

	name = models.CharField(
		max_length=MAX_NAME_LENGTH,
		null=False,
		blank=False,
		validators=[validate_name_has_only_letters_and_spaces,
				   MinLengthValidator(2),],
	)
	
	bio = models.TextField(
		max_length=MAX_BIO_LENGTH,
		null=False,
		blank=False,
		help_text=f"Limit of {MAX_BIO_LENGTH} characters."
	)
	
	primary_specialty = models.CharField(
		max_length=255,
		choices=SPECIALTIES,
		null=False,
		blank=False,
	)
	
	secondary_specialty = models.CharField(
		max_length=255, 
		choices=SPECIALTIES,
		blank=True,
		null=True
	)
	
	years_of_experience = models.IntegerField(
		blank=True,
		null=True
	)
	
	slug = models.SlugField(
		null=False,
		unique=True,
		blank=True
	)
	
	image = ResizedImageField(size=IMAGE_SIZE,
		  crop=['middle', 'center'],
		  quality=85, upload_to='chefs_images/',
		  blank=False, null=False,
		  help_text="Upload an image with a resolution of 400x600 pixels and not bigger than 500kb.",
		  validators = [validate_image_size_less_than_500kb]
	)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(f"{self.name}")
		super(Chef, self).save(*args, **kwargs)

	def get_primary_specialty_display(self):
		return dict(Chef.SPECIALTIES)[self.primary_specialty]

	def get_secondary_specialty_display(self):
		return dict(Chef.SPECIALTIES)[self.secondary_specialty]
