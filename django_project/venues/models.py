from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django_resized import ResizedImageField
from django_project.venues.validators import validate_image_size_less_than_500kb

class Venue(models.Model):

	MAX_NAME_LENGTH = 50
	MAX_LOC_LENGTH = 50
	MAX_DESC_LENGTH = 600
	IMAGE_SIZE = [400, 600]

	name = models.CharField(
		max_length=MAX_NAME_LENGTH,
		null=False,
		blank=False,
	)

	location = models.CharField(
		max_length=MAX_LOC_LENGTH,
		help_text="Enter city and country separated by a comma.",
		null=False,
		blank=False,
		default='Unknown',
	)

	capacity = models.IntegerField(
		blank=False,
		null=False,
		help_text="Enter the maximum number of people that can attend the venue.",
	)

	description = models.TextField(
		max_length=MAX_DESC_LENGTH,
		null=False,
		blank=False,
		help_text=f"Limit of {MAX_DESC_LENGTH} characters.",
	)

	slug = models.SlugField(
		null=False,
		unique=True,
		blank=True
	)
	
	image = ResizedImageField(size=IMAGE_SIZE,
		  crop=['middle', 'center'],
		  quality=85, upload_to='venues_images/',
		  blank=False, null=False,
		  help_text="Upload an image with a resolution of 400x600 pixels and not bigger than 500kb.",
		  validators = [validate_image_size_less_than_500kb]
	)
	
	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(f"{self.name}-{self.capacity}")
		super(Venue, self).save(*args, **kwargs)
