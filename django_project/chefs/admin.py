from django.contrib import admin
from django_project.chefs.models import Chef

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
	list_display = ['name', 'primary_specialty', 'secondary_specialty', 'years_of_experience',]
	list_filter = ['primary_specialty', 'years_of_experience',]
	ordering = ['name', 'primary_specialty',]
	search_fields = ['name', 'bio']