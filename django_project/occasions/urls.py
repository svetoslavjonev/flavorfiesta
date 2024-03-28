from django.urls import path

from django_project.occasions.views import OccasionCreateView, OccasionByMonthYearView

urlpatterns = [
	path('create/', OccasionCreateView.as_view(), name='occasion-create'),
	path('dashboard/', OccasionByMonthYearView.as_view(), name='occasion-dashboard'),
]