from django.shortcuts import render
from .map_form import MapForm
# Create your views here.

def add_map(request):
    if request.method == "POST":
        form = MapForm(request.POST)
        if form.is_valid():
            #creates and saves an object bound to the form
            map_item=form.save(commit=False)
            map_item.save()
    else:
        form = MapForm()
    return render(request, 'maps/map_form.html', {'form':form})  
