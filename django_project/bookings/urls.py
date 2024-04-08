from django.urls import path

from django_project.bookings.views import BookingView, BookingDetailView


urlpatterns = [
	 path('book-occasion/<int:occasion_id>/', BookingView.as_view(), name='book-occasion'),
	 path('booking-details/<int:pk>/', BookingDetailView.as_view(), name='booking-details'),
]