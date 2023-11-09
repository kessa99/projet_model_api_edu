from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import EventForm

def event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre la bourse dans la base de données
            return HttpResponse("Ajout d'un event réussi.")
    else:
        form = EventForm()
    return render(request, 'event.html', {'form': form})
