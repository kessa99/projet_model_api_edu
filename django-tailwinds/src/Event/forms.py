from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'