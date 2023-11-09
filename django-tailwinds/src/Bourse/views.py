from django.shortcuts import render
from django.http import HttpResponse
from .models import Bursary
from .forms import BursaryForm

def bourse(request):
    if request.method == 'POST':
        form = BursaryForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre la bourse dans la base de données
            return HttpResponse("Ajout d'une bourse réussi.")
    else:
        form = BursaryForm()
    return render(request, 'bourse.html', {'form': form})


    