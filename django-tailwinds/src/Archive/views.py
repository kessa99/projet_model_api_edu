from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Archive
from .forms import ArchiveForm

def archive(request):
    if request.method == 'POST':
        form = ArchiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('archive')
    else:
        form = ArchiveForm()
    return render(request, 'archive.html', {'form': form})
