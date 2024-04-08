from django.urls import path
from django_project.api.views import EventListView, ChefListView, VenueListView, OccasionListView

urlpatterns = [
	path('events/', EventListView.as_view(), name='event-list'),
	path('chefs/', ChefListView.as_view(), name='chef-list'),
	path('venues/', VenueListView.as_view(), name='venue-list'),
	path('occasions/', OccasionListView.as_view(), name='occasion-list'),
]