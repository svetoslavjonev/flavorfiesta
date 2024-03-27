from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from django_project.occasions.models import Occasion
from django_project.occasions.forms import OccasionCreateForm


class OccasionCreateView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.CreateView):
	permission_required = 'occasion.add_occasion'
	template_name = 'occasions/occasion-create.html'
	form_class = OccasionCreateForm
	success_url = reverse_lazy('index')
