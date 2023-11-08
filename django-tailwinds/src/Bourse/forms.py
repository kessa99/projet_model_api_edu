from django import forms
from .models import Bursary

class BursaryForm(forms.ModelForm):
    class Meta:
        model = Bursary
        fields = '__all__'