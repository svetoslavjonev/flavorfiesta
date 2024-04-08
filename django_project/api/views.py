from rest_framework import generics as rest_views
from django_project.events.models import Event
from django_project.chefs.models import Chef
from django_project.venues.models import Venue
from django_project.occasions.models import Occasion
from django_project.api.serializers import EventListSerializer, VenueListSerializer, ChefListSerializer, OccasionListSerializer

class EventListView(rest_views.ListAPIView):
	serializer_class = EventListSerializer

	def get_queryset(self):
		queryset = Event.objects.all()
		event_name = self.request.query_params.get('name')
		event_type = self.request.query_params.get('event_type')

		if event_name:
			queryset = queryset.filter(name__icontains=event_name)
		if event_type:
			queryset = queryset.filter(event_type=event_type)

		return queryset


class ChefListView(rest_views.ListAPIView):
	serializer_class = ChefListSerializer

	def get_queryset(self):
		queryset = Chef.objects.all()
		chef_name = self.request.query_params.get('name')
		chef_specialty = self.request.query_params.get('specialty')

		if chef_name:
			queryset = queryset.filter(name__icontains=chef_name)
		if chef_specialty:
			queryset = queryset.filter(primary_specialty=chef_specialty)

		return queryset


class VenueListView(rest_views.ListAPIView):
	serializer_class = VenueListSerializer

	def get_queryset(self):
		queryset = Venue.objects.all()
		venue_name = self.request.query_params.get('name')
		venue_location = self.request.query_params.get('location')

		if venue_name:
			queryset = queryset.filter(name__icontains=venue_name)
		if venue_location:
			queryset = queryset.filter(location__icontains=venue_location)

		return queryset


class OccasionListView(rest_views.ListAPIView):
	queryset = Occasion.objects.select_related('event', 'venue', 'chef').all()
	serializer_class = OccasionListSerializer

