from django.shortcuts import render
from django.http import HttpResponse
from .models import Bursary
from .forms import BursaryForm

def save_bourse(request):
    if request.method == 'POST':
        form = BursaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Enregistre la bourse dans la base de données
            return render(request, 'bourses/print_bourse.html', {})
    else:
        form = BursaryForm()
    return render(request, 'bourses/save_bourse.html', {'form': form})


def print_bourse(request):
    bourses = Bursary.objects.all()
    return render(request, 'bourses/print_bourse.html', {"bourses": bourses})
    