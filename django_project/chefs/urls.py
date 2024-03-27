from django.urls import path

from django_project.chefs.views import ChefDashboardView, ChefDetailsView, ChefCreateView, ChefEditView, ChefDeleteView

urlpatterns = [
	path('', ChefDashboardView.as_view(), name='chef-dashboard'),
	path('details/<int:pk>/<slug:slug>/', ChefDetailsView.as_view(), name='chef-details'),
	path('create/', ChefCreateView.as_view(), name='chef-create'),
	path('edit/<int:pk>/<slug:slug>/', ChefEditView.as_view(), name='chef-edit'),
	path('delete/<int:pk>/<slug:slug>/', ChefDeleteView.as_view(), name='chef-delete'),
]
