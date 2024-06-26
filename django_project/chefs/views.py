from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import get_object_or_404
from django.utils import timezone

from django_project.chefs.models import Chef
from django_project.chefs.forms import ChefForm
from django_project.occasions.models import Occasion


class ChefDashboardView(auth_mixin.LoginRequiredMixin, views.TemplateView):
	login_url = "/profiles/signin-user/"
	template_name = 'chefs/chef-dashboard.html'
	model = Chef

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['object_list'] = Chef.objects.order_by('pk')
		return context


class ChefDetailsView(auth_mixin.LoginRequiredMixin, views.TemplateView):
	login_url = "/profiles/signin-user/"
	template_name = 'chefs/chef-details.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		chef_id = self.kwargs.get('pk')
		context['chef'] = get_object_or_404(Chef, pk=chef_id)
		context['next_occasions'] = Occasion.objects.filter(
			chef=context['chef'], 
			start_time__gte=timezone.now()
		).order_by('start_time')[:5]
		return context


class ChefCreateView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.CreateView):
	permission_required = 'chefs.add_chef'
	login_url = "/profiles/signin-user/"
	template_name = 'chefs/chef-create.html'
	form_class = ChefForm

	def get_success_url(self):
		return reverse_lazy('chef-details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class ChefEditView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.UpdateView):
	permission_required = 'chefs.change_chef'
	login_url = "/profiles/signin-user/"
	model = Chef
	template_name = 'chefs/chef-edit.html'
	form_class = ChefForm

	def get_success_url(self):
		return reverse_lazy('chef-details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class ChefDeleteView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.DeleteView):
	permission_required = 'chefs.delete_chef'
	login_url = "/profiles/signin-user/"
	model = Chef
	template_name = 'chefs/chef-delete.html'

	def get_success_url(self):
		return reverse_lazy('chef-dashboard')
