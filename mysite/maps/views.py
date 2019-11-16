from django.shortcuts import render, redirect
#from .map_form import MapForm
from .models import Building, MapForm, Map
from haversine import haversine, Unit

# Create your views here.

def add_map(request, id=id):
    if request.method == "POST":
        form = MapForm(request.POST)
        if form.is_valid():
            #creates and saves an object bound to the form
            map_item=form.save(commit=False)
            map_item.save()

            user_buildings=[]
            user_buildings.append(Building.objects.get(name=form.cleaned_data['building1']))
            user_buildings.append(Building.objects.get(name=form.cleaned_data['building2']))
            user_buildings.append(Building.objects.get(name=form.cleaned_data['building3']))
            user_buildings.append(Building.objects.get(name=form.cleaned_data['building4']))
            user_buildings.append(Building.objects.get(name=form.cleaned_data['building5']))

            bldg1 = Building.objects.get(name=form.cleaned_data['building1'])
            print(bldg1.latitude)

            print(user_buildings)
            
            global global_distances
            distances = []
            for i in range(0, len(user_buildings)-1):
                b1=user_buildings[i]
                b2=user_buildings[i+1]
                distances.append(round(haversine((b1.latitude, b1.longitude), (b2.latitude, b2.longitude)), 4))

            global_distances = distances[:]
            print(distances)

            return redirect('/maps/' + str(map_item.id) + '/')
    else:
        form = MapForm()

    return render(request, 'maps/map_form.html', {'form':form})  


def distance_output(request, id=id):
    context = {
        'map':Map.objects.get(id=id),
        'all_buildings': Building.objects.all(),
        'distances':global_distances,
    }

    return render(request, 'maps/map.html', context=context)

def shortest_distance(lat1, long1, lat2, long2):
    return haversine((lat1, long1), (lat1, lat2), unit=Unit.MILES)

def shortest_distance(lat1, long1, lat2, long2):
    return haversine((lat1, long1), (lat1, lat2), unit=Unit.MILES)