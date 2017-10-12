from django import forms
from .models import Participants

class ParticipantForm(forms.ModelForm):
	class Meta:
		model = Participants
		exclude = ('registration_id',)


