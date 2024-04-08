from rest_framework import serializers
from django_project.occasions.models import Occasion, Seat
from django_project.chefs.models import Chef
from django_project.venues.models import Venue
from django_project.events.models import Event

class ChefListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chef
		fields = ['name', 'primary_specialty', 'secondary_specialty', 'bio']

class VenueListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Venue
		fields = ['name', 'location', 'capacity', 'description']

class EventListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ['name', 'event_type', 'description']

# Nested Serializers for Occasion
class EventNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ['name']

class VenueNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Venue
		fields = ['name']

class ChefNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chef
		fields = ['name']

class OccasionListSerializer(serializers.ModelSerializer):
	event = EventNameSerializer(read_only=True)
	venue = VenueNameSerializer(read_only=True)
	chef = ChefNameSerializer(read_only=True)

	class Meta:
		model = Occasion
		fields = ['event', 'venue', 'chef', 'start_time', 'end_time']