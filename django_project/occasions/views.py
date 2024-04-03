from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
import datetime

from django_project.occasions.models import Occasion
from django_project.occasions.forms import OccasionCreateForm, MonthYearForm, OccasionEditForm


class OccasionCreateView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.CreateView):
	permission_required = 'occasion.add_occasion'
	template_name = 'occasions/occasion-create.html'
	form_class = OccasionCreateForm
	success_url = reverse_lazy('index')


class OccasionByMonthYearView(auth_mixin.LoginRequiredMixin, views.FormView):
	template_name = 'occasions/occasion-dashboard.html'
	form_class = MonthYearForm

	def form_valid(self, form):
		context = self.get_context_data()
		month_year = form.cleaned_data['month_year']
		month, year = month_year.split(', ')
		year = int(year)

		month = datetime.datetime.strptime(month, "%B").month
		today = datetime.datetime.today()
		if int(year) == today.year and month == today.month:
			context['occasions'] = Occasion.objects.filter(
				start_time__year=year,
				start_time__month=month,
				start_time__gte=datetime.datetime.now()  # Compare with current datetime to filter out past events
			).order_by('start_time')
		else:
			context['occasions'] = Occasion.objects.filter(
				start_time__year=year,
				start_time__month=month
			).order_by('start_time')
		return self.render_to_response(context)

	def get_context_data(self, **kwargs):
		context = super(OccasionByMonthYearView, self).get_context_data(**kwargs)
		if 'occasions' not in context:
			# This is the initial load; no form submission has happened yet.
			# Fetch occasions for the default month and year.
			default_month_year = self.form_class().fields['month_year'].initial
			month, year = default_month_year.split(', ')
			year = int(year)
			month = datetime.datetime.strptime(month, "%B").month
			today = datetime.datetime.today()
			if int(year) == today.year and month == today.month:
				context['occasions'] = Occasion.objects.filter(
					start_time__year=year,
					start_time__month=month,
					start_time__gte=datetime.datetime.now()  # Compare with current datetime to filter out past events
				).order_by('start_time')
			else:
				context['occasions'] = Occasion.objects.filter(
					start_time__year=year,
					start_time__month=month
				).order_by('start_time')
		return context

class OccasionEditView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.UpdateView):
	permission_required = 'occasions.change_occasion'
	model = Occasion
	template_name = 'occasions/occasion-edit.html'
	form_class = OccasionEditForm

	def get_success_url(self):
		return reverse_lazy('occasion-dashboard')

class OccasionDeleteView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.DeleteView):
	permission_required = 'occasions.delete_occasion'
	model = Occasion
	template_name = 'occasions/occasion-delete.html'

	def get_success_url(self):
		return reverse_lazy('occasion-dashboard')