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



def liste_bourse(request):
    bourse = Bourse.objects.all()
    return render(request, 'bourses/liste_bourse.html', {'bourse': bourse})

def liste_bourse_admin(request):
    bourse = Bourse.objects.all()
    return render(request, 'bourses/liste_bourse_admin.html', {'bourse': bourse})



def details_bourse(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    postulants = Postulant.objects.filter(bourse=bourse)
    commentaire = Commentaire.objects.filter(bourse=bourse)
    return render(request, 'bourses/detail_bourse.html', {'bourse': bourse, 'postulants': postulants, 'commentaire':commentaire})

def details_bourse_admin(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    postulants = Postulant.objects.filter(bourse=bourse)
    commentaire = Commentaire.objects.filter(bourse=bourse)
    return render(request, 'bourses/detail_bourse_admin.html', {'bourse': bourse, 'postulants': postulants, 'commentaire':commentaire})




def modifie_bourse(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    if request.method =='POST':
        form = BourseForm(request.POST, instance=bourse)
        if form.is_valid():
            form.save()
            return redirect('details_bourse_admin', bourse_id=bourse_id)
    else:
        form = BourseForm(instance=bourse)
    context = {
        'form': form,
        'bourse': bourse,
    }
    return render(request, 'bourses/modifie_bourse.html', context)


def supprime_bourse(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    if request.method == 'POST':
        bourse.delete()
        return redirect('liste_bourse')
    return render(request, 'bourses/supprime_bourse.html', {'bourse': bourse})

# etre en mesure de postuler, afficher la listes des postulant
def saisir_postulant(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)

    if request.method == 'POST':
        form = PostulerForm(request.POST)
        if form.is_valid():
            postulant = form.save(commit=False)
            postulant.bourse = bourse
            postulant.save()
            return redirect('detail_bourse', bourse_id=bourse_id)
    else:
        form = PostulerForm()
    context = {
        'form': form,
        'bourse': bourse,
    }
    return render(request, 'bourses/saisir_postulant.html', context)




def liste_postulant(request, bourse_id):
    postulant = Postulant.objects.filter(bourse_id=bourse_id)
    return render(request, 'bourses/liste_postulant.html', {'postulant': postulant})


# saisir les Commentaire afficher les Commentaire

def saisie_commentaire(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)

        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.bourse = bourse
            commentaire.nom = request.user
            commentaire.save()
            return redirect('details_bourse', bourse_id=bourse_id)
    else:
        context = {
            'form': form,
            'bourse': bourse
        }
        form = CommentaireForm()
    return render(request, 'bourses/saisir_commentaire.html', context)