from django.urls import path

from django_project.tickets.views import TicketCreateView

urlpatterns = [
	path('create/', TicketCreateView.as_view(), name='ticket-create'),
]