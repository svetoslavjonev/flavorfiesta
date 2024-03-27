from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_project.profiles.validators import validate_name_has_only_letters


class AppUser(AbstractUser):

    MAX_FIRST_NAME_LENGTH = 30

    MAX_LAST_NAME_LENGTH = 30

    email = models.EmailField(unique=True, null=False, blank=False)

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(MinLengthValidator(2),
					validate_name_has_only_letters),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            MinLengthValidator(2),
            validate_name_has_only_letters,
        ),
        null=True,
        blank=True,
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ),
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name
