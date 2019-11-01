from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .maps_form import mapsForm
from .maps_form import DistanceForm

# Create your views here.

def index(request):
    return render_to_response('index.html')

#def maps(request):
#    return render_to_response('maps.html')

def ratings_landing_page(request):
    return render_to_response('ratings_landing_page.html')

def rating_form(request):
    return render_to_response('rating_form.html')

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
    #return render(request, 'maps_form.html', {'form':form})

def distance(request):
    if request.method=="POST":
        form = DistanceForm(request.POST)
        if form.is_valid():
            #return an object that has not been saved in the database yet
            item=form.save(commit=False)

            #save the object
            item.save()
        else:
            #unbound form with no data
            form=DistanceForm
        return render(request, 'maps_form.html', {'form':form})