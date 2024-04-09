from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django_resized import ResizedImageField
from django_project.events.validators import validate_image_size_less_than_500kb


UserModel = get_user_model()


class Event(models.Model):

	MAX_TYPE_LENGTH = 20
	MAX_NAME_LENGTH = 60
	MAX_DESCRIPTION_LENGTH = 600
	IMAGE_SIZE = [400, 600]
	
	EVENT_TYPES = (
		('tasting_event', 'Tasting Event'),
		('cooking_class', 'Cooking Class'),
	)
	
	event_type = models.CharField(max_length=MAX_TYPE_LENGTH,
								  choices=EVENT_TYPES,
								  default='cooking_class',
								  blank=False,
								  null=False,)
	
	name = models.CharField(
		max_length=MAX_NAME_LENGTH,
		null=False,
		blank=False,)
	
	description = models.TextField(
		max_length=MAX_DESCRIPTION_LENGTH,
		null=False,
		blank=False,
		help_text=f"Limit of {MAX_DESCRIPTION_LENGTH} characters."
	)
	
	slug = models.SlugField(null=False, unique=True, blank=True)
	
	image = ResizedImageField(size=IMAGE_SIZE,
							  crop=['middle', 'center'],
							  quality=85, upload_to='events_images/',
							  blank=False, null=False,
							  help_text="Upload an image with a resolution of 400x600 pixels and not bigger than 500kb.",
							  validators = [validate_image_size_less_than_500kb])

	def __str__(self):
		return f"{self.name} - {self.event_type}"

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(f"{self.name}")
		super(Event, self).save(*args, **kwargs)

	def get_event_type_display(self):
		return dict(Event.EVENT_TYPES)[self.event_type]


class EventComment(models.Model):

	MAX_COMMENT_LENGTH = 400
	
	content = models.CharField(
		max_length=MAX_COMMENT_LENGTH,
		null=False,
		blank=False,
	)
	
	created_at = models.DateTimeField(
		auto_now_add=True,
		blank=True,
		null=False,
	)
	
	event = models.ForeignKey(
		Event,
		on_delete=models.CASCADE,
		null=False,
		blank=False,
	)
	
	user = models.ForeignKey(
		UserModel,
		on_delete=models.CASCADE,
		null=False,
		blank=False,
	)
	
