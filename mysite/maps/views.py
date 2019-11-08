from django.shortcuts import render, redirect
#from .map_form import MapForm
from .models import Building
# Create your views here.
"""
def add_map(request):
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
"""
def building(request, id=id):
    build=Building()
    return render(request, 'maps/map.html', {'build':build})