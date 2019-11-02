from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from .maps_form import MapForm
#from .maps_form import Distance
from .rate_forms import RateForm

# Create your views here.

def index(request):
    return render_to_response('index.html')

#def maps(request):
#    return render_to_response('maps.html')

def ratings_landing_page(request):
#def index1(request):
    return render_to_response('ratings_landing_page.html')
    #return render_to_response('index1.html')


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
"""
def distance(request):
    if request.method=="POST":
        form = MapForm(request.POST)
        if form.is_valid():
            #return an object that has not been saved in the database yet
            item=form.save(commit=False)

            #save the object
            item.save()
        else:
            #unbound form with no data
            form=MapForm
        #return render(request, 'maps_form.html', {'form':form})
    return render(request, 'maps_form.html', {'form':form})
"""
def advice(request):
     return render_to_response('advice.html')

def upload_video(request):
     return render_to_response('upload_video.html')

def view_video(request):
     return render_to_response('view_video.html')

def time(request):
      return render_to_response('time.html')

def rating_form(request):
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            class_rated=form.cleaned_data['class_rated']
            class_difficulty_level=form.cleaned_data['class_difficulty_level']
            class_hours_spent=form.cleaned_data['class_hours_spent']
            rater_grade=form.cleaned_data['rater_grade']
            class_exams_num=form.cleaned_data['class_exams_num']
            class_hw=form.cleaned_data['class_hw']
            class_comments=form.cleaned_data['class_comments']
            class_overall=form.cleaned_data['class_overall']
            print(class_rated,class_difficulty_level,class_hours_spent,rater_grade,class_exams_num,class_hw,class_comments,class_overall);
            #it will go to view rating if successful
            return HttpResponseRedirect('/ratings_view.html/')
    else:
        form = RateForm()
    return render(request, 'rating_form.html', {'form': form})
