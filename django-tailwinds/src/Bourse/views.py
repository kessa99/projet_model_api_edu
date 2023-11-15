from django.shortcuts import render, get_object_or_404, redirect
from .models import Bourse, Postulant, Commentaire
from .forms import BourseForm, PostulerForm, CommentaireForm

# Saisir bourse, lister les bourses afficher les details de la bourse
def saisie_bourse(request):
    if request.method == 'POST':
        form = BourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'bourses/liste_bourse.html', {})
    else:
        form = BourseForm()
    return render(request, 'bourses/saisir_bourse.html', {'form': form})

def liste_bourses(request):
    bourses = Bourse.objects.all()
    return render(request, 'bourses/liste_bourse.html', {'bourses': bourses})

def detail_bourse(request, bourse_id):
    bourses = get_object_or_404(Bourse, pk=bourse_id)
    postulants = Postulant.objects.filter(bourses=bourses)
    commentaire = Commentaire.objects.filter(bourses=bourses)
    return render(request, 'bourses/detail_bourse.html', {'bourses': bourses, 'postulants': postulants, 'commentaire':commentaire})




# etre en mesure de postuler, afficher la listes des postulant
def saisie_postulant(request, bourse_id):
    bourses = get_object_or_404(Bourse, pk=bourse_id)

    if request.method == 'POST':
        form = PostulerForm(request.POST)
        if form.is_valid():
            postulant = form.save(commit=False)
            postulant.bourses = bourses
            postulant.save()
            return redirect('detail_bourse', bourse_id=bourse_id)
    else:
        form=PostulerForm()
    return(request, 'saisir_postulant.html', {'form':form, 'bourses':bourses})

def liste_postulant(request):
    postulant = Postulant.objects.all()
    return render(request, 'bourses/liste_postulant.html', {'postulant':postulant})



# saisir les Commentaire afficher les Commentaire
# @login_required
def saisir_commentaire(request, bourse_id):
    bourses = get_object_or_404(Bourse, pk=bourse_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.bourses = bourses
            commentaire.nom = request.user.username
            commentaire.save()
            return redirect('details_bourse', bourse_id=bourse_id)
    else:
        form = CommentaireForm()
    return render(request, 'bourses/saisir_commentaire.html', {'form': form, 'bourses': bourses})