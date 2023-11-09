from django.shortcuts import render
from django.http import HttpResponse
from .models import Archive
from .forms import ArchiveForm

def archive(request):
    if request.method == 'POST':
        form = ArchiveForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre la bourse dans la base de données
            return HttpResponse("Ajout d'une archive réussi.")
    else:
        form = ArchiveForm()
    return render(request, 'archive.html', {'form': form})
