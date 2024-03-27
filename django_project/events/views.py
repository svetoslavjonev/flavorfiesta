from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import get_object_or_404

from django_project.events.models import Event, EventComment
from django_project.events.forms import EventForm, EventCommentForm


class EventDashboardView(auth_mixin.LoginRequiredMixin, views.TemplateView):
	template_name = 'events/event-dashboard.html'
	model = Event

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['object_list'] = Event.objects.order_by('pk')
		return context


class EventDetailsView(auth_mixin.LoginRequiredMixin, views.TemplateView):
	template_name = 'events/event-details.html'

	def get(self, request, pk, slug):
		event = Event.objects.filter(pk=pk, slug=slug).get()
		comment_form = EventCommentForm()
		comments = EventComment.objects.filter(event_id=pk).order_by('-created_at')
		
		context = {
			'event': event,
			'comment_form': comment_form,
			'comments': comments,
		}

		return render(request, 'events/event-details.html', context)

	def post(self, request, pk, slug):
		event = Event.objects.filter(pk=pk, slug=slug).get()

		comment_form = EventCommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			comment.event = event
			comment.user = self.request.user
			comment.save()
			return redirect('{}#comments-list'.format(reverse('event-details', kwargs={'pk': pk, 'slug': slug})))

		else:
			return redirect('index')


class EventCreateView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.CreateView):
	permission_required = 'events.add_event'
	template_name = 'events/event-create.html'
	form_class = EventForm

	def get_success_url(self):
		return reverse_lazy('event-details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class EventEditView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.UpdateView):
	permission_required = 'events.change_event'
	model = Event
	template_name = 'events/event-edit.html'
	form_class = EventForm

	def get_success_url(self):
		return reverse_lazy('event-details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class EventDeleteView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.DeleteView):
	permission_required = 'events.delete_event'
	model = Event
	template_name = 'events/event-delete.html'
	
	def get_success_url(self):
		return reverse_lazy('event-dashboard')


class EditCommentView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.UpdateView):
	permission_required = 'eventcomment.change_eventcomment'
	template_name = 'events/comment-edit.html'
	model = EventComment
	fields = ('content',)

	def get_success_url(self):
		event = Event.objects.filter(pk=self.object.event_id).get()
		return '{}#comments-list'.format(reverse('event-details', kwargs={'pk': event.pk, 'slug': event.slug}))


class DeleteCommentView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.DeleteView):
	permission_required = 'eventcomment.delete_eventcomment'
	template_name = 'events/comment-delete.html'
	model = EventComment

	def get_success_url(self):
		event = Event.objects.filter(pk=self.object.event_id).get()
		return '{}#comments-list'.format(reverse('event-details', kwargs={'pk': event.pk, 'slug': event.slug}))