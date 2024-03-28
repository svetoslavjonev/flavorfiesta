from django.urls import path

from django_project.occasions.views import OccasionCreateView, OccasionByMonthYearView, OccasionEditView, OccasionDeleteView

urlpatterns = [
	path('create/', OccasionCreateView.as_view(), name='occasion-create'),
	path('dashboard/', OccasionByMonthYearView.as_view(), name='occasion-dashboard'),
	path('edit/<int:pk>/', OccasionEditView.as_view(), name='occasion-edit'),
	path('delete/<int:pk>/', OccasionDeleteView.as_view(), name='occasion-delete'),
]