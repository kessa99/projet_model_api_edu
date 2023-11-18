from django import forms
from .models import Archive, Commentaire

class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = '__all__'

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = '__all__'
    