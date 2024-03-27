from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import get_object_or_404

from django_project.venues.models import Venue
from django_project.venues.forms import VenueForm


class VenueDashboardView(auth_mixin.LoginRequiredMixin, views.TemplateView):
	template_name = 'venues/venue-dashboard.html'
	model = Venue

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['object_list'] = Venue.objects.order_by('pk')
		return context

class VenueDetailsView(auth_mixin.LoginRequiredMixin, views.TemplateView):
	template_name = 'venues/venue-details.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		venue_id = self.kwargs.get('pk')
		context['venue'] = get_object_or_404(Venue, pk=venue_id)
		return context

class VenueCreateView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.CreateView):
	permission_required = 'venues.add_venue'
	template_name = 'venues/venue-create.html'
	form_class = VenueForm

	def get_success_url(self):
		return reverse_lazy('venue-details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

class VenueEditView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.UpdateView):
	permission_required = 'venues.change_venue'
	model = Venue
	template_name = 'venues/venue-edit.html'
	form_class = VenueForm

	def get_success_url(self):
		return reverse_lazy('venue-details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

class VenueDeleteView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.DeleteView):
	permission_required = 'venues.delete_venue'
	model = Venue
	template_name = 'venues/venue-delete.html'

	def get_success_url(self):
		return reverse_lazy('venue-dashboard')

