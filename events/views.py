from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .forms import ParticipantForm
# Create your views here.

class ParticipantCreate(CreateView):
	template_name = 'events/participant_form.html'
	success_url = reverse_lazy('add_participants')
	form_class = ParticipantForm

	def form_valid(self, form):
		mar_user = self.request.user
		event = form.cleaned_data['event']
		mar_user.total += event.price
		mar_user.save()
		
		form.save()
		return HttpResponseRedirect(self.success_url)
