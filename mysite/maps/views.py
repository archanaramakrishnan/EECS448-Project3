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
            
            #context = { 'distances': distances }

            return redirect('/maps/' + str(map_item.id) + '/')
    else:
        form = MapForm()

    user_buildings=[]
    user_buildings.append(Building.objects.get(name=form.cleaned_data['building1']))
    user_buildings.append(Building.objects.get(name=form.cleaned_data['building2']))
    user_buildings.append(Building.objects.get(name=form.cleaned_data['building3']))
    user_buildings.append(Building.objects.get(name=form.cleaned_data['building4']))
    user_buildings.append(Building.objects.get(name=form.cleaned_data['building5']))

    bldg1 = Building.objects.get(name=form.cleaned_data['building1'])
    print(bldg1.latitude)

    print(user_buildings)
    
    distances = []
    for i in range(0, len(user_buildings)-1):
        distances.append(haversine((user_buildings[i].latitude, user_buildings[i].longitude), (user_buildings[i+1].latitude, user_buildings[i+1].longitude)))

    print(distances)

    context = {
        'form':MapForm(request.POST),
        'distances': distances,
    }

    return render(request, 'maps/map_form.html', context=context)  


def distance_output(request, id=id):
    context = {
        'map':Map.objects.get(id=id),
        'all_buildings': Building.objects.all(),
    }

    return render(request, 'maps/map.html', context=context)

def shortest_distance(lat1, long1, lat2, long2):
    return haversine((lat1, long1), (lat1, lat2), unit=Unit.MILES)

    
"""
def building(request, id=id):
    build=Building()
    return render(request, 'maps/ind.html', {'build':build})

def form_view(request):
    context = {
        'all_buildings': Building.objects.all()
    }

    if request.POST:
        building_pk_list = request.POST.getlist('building', None)
        print(request.POST.getlist('building', None))

        selected_building_obj_list = Building.objects.filter(pk__in=building_pk_list)
        print(selected_building_obj_list)


    return render(request, 'maps/index.html', context=context)

def distance_calculator(request):
    context = {
        'all_buildings': Building.objects.all()
    }

    return render(request, 'maps/distance.html', context=context)
"""