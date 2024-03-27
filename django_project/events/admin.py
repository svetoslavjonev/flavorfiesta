from django.contrib import admin
from django_project.events.models import Event, EventComment

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ['name', 'event_type']
	list_filter = ["event_type",]
	ordering = ['name', 'event_type']
	search_fields = ['name', 'description']


@admin.register(EventComment)
class EventCommentAdmin(admin.ModelAdmin):
	list_display = ['user', 'event', 'content']
	list_filter = ['event', 'user']
	ordering = ['created_at']
	search_fields = ['user__username', 'event__name', 'content']

