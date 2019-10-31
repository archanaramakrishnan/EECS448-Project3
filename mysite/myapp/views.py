from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .maps_form import mapsForm
from .rate_forms import RateForm

# Create your views here.

def index(request):
    return render_to_response('index.html')

#def maps(request):
#    return render_to_response('maps.html')

def ratings_landing_page(request):
    return render_to_response('ratings_landing_page.html')


def ratings_view(request):
    return render_to_response('ratings_view.html')

def maps(request):
    if request.method == "POST":
        form = mapsForm(request.POST)
        if form.is_valid():
            building1=form.cleaned_data['building1']
            building2=form.cleaned_data['building2']
            building3=form.cleaned_data['building3']
            building4=form.cleaned_data['building4']

            print(building1, building2, building3, building4)

    form = mapsForm()
    return render(request, 'maps_form.html', {'form':form})


def rating_form(request):
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            print(name);
    form = RateForm()
    return render(request, 'rating_form.html', {'form': form})
