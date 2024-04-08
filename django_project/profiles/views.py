from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms
from django.utils.dateformat import format
from django.conf import settings
from django.utils import timezone

from django_project.profiles.forms import UserCreateForm, ProfileEditForm
from django_project.bookings.models import Booking

UserModel = get_user_model()


class OwnerRequiredMixin(auth_mixin.AccessMixin):
	"""Verify that the current user has this profile."""

	def dispatch(self, request, *args, **kwargs):
		if request.user.pk != kwargs.get('pk', None):
			return self.handle_no_permission()
		return super().dispatch(request, *args, **kwargs)


class SignInUserView(auth_views.LoginView):
    template_name = "profiles/user-signin.html"
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


def signout_user(request):
    logout(request)
    return redirect('index')


class SignUpUserView(views.CreateView):
    template_name = "profiles/user-signup.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):

        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


class ProfileDetailsView(OwnerRequiredMixin, views.DetailView):
	template_name = "profiles/profile-details.html"
	model = UserModel
	
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# Assuming self.object is a User instance. Adjust if necessary.
		context['is_owner'] = self.request.user == self.object
		context['next_bookings'] = Booking.objects.filter(
			user=self.object,
			occasion__start_time__gte=timezone.now()  # Note the double underscore for accessing related fields.
		).order_by('occasion__start_time')[:5]  # Adjusted ordering field.
		return context


class ProfileEditView(OwnerRequiredMixin, views.UpdateView):
	template_name = "profiles/profile-edit.html"
	model = UserModel
	form_class = ProfileEditForm

	def get_success_url(self):
		return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk, })

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['is_owner'] = self.request.user == self.object
		return context



class ProfileDeleteView(OwnerRequiredMixin, views.DeleteView):
    template_name = 'profiles/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context
