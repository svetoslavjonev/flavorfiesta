from django.urls import path

from django_project.events.views import EventDashboardView, EventDetailsView, EventCreateView, EventEditView, EventDeleteView, EditCommentView, DeleteCommentView

urlpatterns = [
	path('', EventDashboardView.as_view(), name='event-dashboard'),
	path('details/<int:pk>/<slug:slug>/', EventDetailsView.as_view(), name='event-details'),
	path('create/', EventCreateView.as_view(), name='event-create'),
	path('edit/<int:pk>/<slug:slug>/', EventEditView.as_view(), name='event-edit'),
	path('delete/<int:pk>/<slug:slug>/', EventDeleteView.as_view(), name='event-delete'),
	path('comment/<int:pk>/edit/', EditCommentView.as_view(), name='comment-edit'),
	path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='comment-delete'),
	
]
