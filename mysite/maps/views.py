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



            return redirect('/maps/' + str(map_item.id) + '/')
    else:
        form = MapForm()

    return render(request, 'maps/map_form.html', {'form':form})  


def map(request, id=id):
    map=Map.objects.get(id=id)
    return render(request, 'maps/map.html', {'map':map})

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