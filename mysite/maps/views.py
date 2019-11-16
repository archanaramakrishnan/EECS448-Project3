from django.shortcuts import render, redirect
from .models import Building, MapForm, Map
from haversine import haversine, Unit

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
            
            global global_distances
            global_distances = []
            for i in range(0, len(user_buildings)-1):
                b1=user_buildings[i]
                b2=user_buildings[i+1]
                global_distances.append(round(haversine((b1.latitude, b1.longitude), (b2.latitude, b2.longitude), unit=Unit.MILES), 4))

            distances = global_distances[:]

            print(distances)

            global global_times
            global_times = []

            #average walking speed in miles/minutes of people in their 20s
            avg_speed = 0.05033333

            for distance in distances:
                global_times.append(round(distance/avg_speed, 4))

            #print(global_times)

            return redirect('/maps/' + str(map_item.id) + '/')
    else:
        form = MapForm()

    return render(request, 'maps/map_form.html', {'form':form})  
"""
def shortest_distance(lat1, long1, lat2, long2):
    return haversine((lat1, long1), (lat1, lat2), unit=Unit.MILES)

def walking_time():
    distances = global_distances[:]

    global times
    times = []

    #average walking speed in miles/minutes of people in their 20s
    avg_speed = 0.05033333

    for distance in distances:
        times.append(distance/avg_speed)

    print(times)
"""
def distance_output(request, id=id):
    context = {
        'map':Map.objects.get(id=id),
        'all_buildings': Building.objects.all(),
        'distances':global_distances,
        'walking_times':global_times
    }

    print(global_distances)
    print(global_times)

    return render(request, 'maps/map.html', context=context)