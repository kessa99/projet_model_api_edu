from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Event
from .forms import EventForm

def saisie_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("liste_event.")
    else:
        form = EventForm()
    return render(request, 'event/saisie_event.html', {'form': form})


def liste_event(request):
    event = Event.objects.all()
    return render(request, 'event/liste_event.html', {'event': event})

def liste_event_admin(request):
    event = Event.objects.all()
    return render(request, 'event/liste_event_admin.html', {'event': event})


def detail_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/detail_event.html', {'event': event})

def detail_event_admin(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/detail_event_admin.html', {'event': event})




def modifie_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('detail_event', event_id=event_id)
    else:
        context = {
            'form': form,
            'event':event,
        }
    return render(request, 'event/modifie_event.html', context)





def supprime_event(request, event_id):
    event = get_object_or_404(event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('list_event')
    return render(request, 'event/supprimet_event.thml', {'event':event})

