from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Archive, Commentaire
from .forms import ArchiveForm, CommentaireForm

def saisie_archive(request):
    if request.method == 'POST':
        form = ArchiveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_archive')
    else:
        form = ArchiveForm()
    return render(request, 'archive/saisie_archive.html', {'form': form})




def liste_archive(request):
    archive = Archive.objects.all()
    return render(request, 'archive/liste_archive.html', {'archive': archive})

def liste_archive_admin(request):
    archive = Archive.objects.all()
    return render(request, 'archive/liste_archive_admin.html', {'archive': archive})




def detail_archive(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    return render(request, 'archive/detail_archive.html', {'archive': archive})

def detail_archive_admin(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    return render(request, 'archive/detail_archive_admin.html', {'archive': archive})




def modifie_archive(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    if request.method =='POST':
        form = ArchiveForm(request.POST, instance=archive)
        if form.is_valid():
            form.save()
            return redirect('detail_archive_admin', archive_id=archive_id)
    else:
        form = ArchiveForm(instance=archive)
    context = {
        'form': form,
        'archive': archive,
    }
    return render(request, 'archive/modifie_archive.html', context)



def supprime_archive(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    if request.method == 'POST':
        archive.delete()
        return redirect('liste_archive')
    return render(request, 'archive/supprime_archive.html', {'archive': archive})






def commentaire_archive(request, archive_id):
    archive = get_list_or_404(Archive, pk=archive_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = Commentaire(
                archive=archive,
                contenu=form.cleaned_data['contenu']
            )
            commentaire.save()
    return redirect('detail_archive', archive_id=archive_id)