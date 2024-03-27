from django.urls import path

from django_project.venues.views import VenueDashboardView, VenueDetailsView, VenueCreateView, VenueEditView, VenueDeleteView

urlpatterns = [
	path('', VenueDashboardView.as_view(), name='venue-dashboard'),
	path('details/<int:pk>/<slug:slug>/', VenueDetailsView.as_view(), name='venue-details'),
	path('create/', VenueCreateView.as_view(), name='venue-create'),
	path('edit/<int:pk>/<slug:slug>/', VenueEditView.as_view(), name='venue-edit'),
	path('delete/<int:pk>/<slug:slug>/', VenueDeleteView.as_view(), name='venue-delete'),
]