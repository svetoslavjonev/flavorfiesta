from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from django_project.tickets.forms import TicketForm


class TicketCreateView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.CreateView):
	login_url = "/profiles/singin-user/"
	permission_required = 'tickets.add_ticket'
	form_class = TicketForm
	template_name = 'tickets/ticket-create.html'
	success_url = reverse_lazy('index')