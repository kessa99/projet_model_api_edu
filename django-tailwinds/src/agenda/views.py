from django.shortcuts import render
from .models import Agenda
from .forms import AgendaForm 
# Create your views here.

def agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AgendaForm()
    return render(request, 'agenda.html', {'form': form})