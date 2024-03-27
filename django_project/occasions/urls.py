from django.urls import path

from django_project.occasions.views import OccasionCreateView

urlpatterns = [
	path('create/', OccasionCreateView.as_view(), name='occasion-create'),
]