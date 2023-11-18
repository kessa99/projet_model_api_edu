from django import forms
from .models import Bourse, Postulant, Commentaire

class BourseForm(forms.ModelForm):
    class Meta:
        model = Bourse
        fields = '__all__'

class PostulerForm(forms.ModelForm):
    class Meta:
        model = Postulant
        fields = ['nom', 'email', 'contenu']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CommentaireForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget = forms.HiddenInput()
