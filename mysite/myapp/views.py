from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from .maps_form import mapsForm
#from .rate_forms import RateForm
from .models import Post
from .advice_form import PostForm
from .models import Rate
from .rate_forms import RateForm
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.

def index(request):
    """
    Directs to index.html page

    **Template:**

    :template:`myapp/index.html`
    """
    return render_to_response('index.html')

#def maps(request):
#    return render_to_response('maps.html')

def ratings_landing_page(request):
    """
    Directs to the landing page for Rate My Class

    **Template:**

    :template:`myapp/ratings_landing_page.html`
    """
    return render_to_response('ratings_landing_page.html')
    #return render_to_response('index1.html')


def ratings_view(request):
    """
    Directs to the page to where you can choose from classes

    **Template:**

    :template:`myapp/ratings_view.html`
    """
    return render_to_response('ratings_view.html')

def ratings_view_class(request):
    """
    Directs to the page to view class ratings

    **Template:**

    :template:`myapp/ratings_view_class.html`
    """
    return render_to_response('ratings_view_class.html')

def maps(request):
    """
    Directs to form for the maps page

    **Template:**

    :template:`myapp/maps_form.html`
    """
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

def advice(request):
    """
    Directs to advice homepage

    **Template:**

    :template:`myapp/advice.html`
    """
    return render_to_response('advice.html')

def upload_video(request):
    """
    Directs to upload video page

    **Template:**

    :template:`myapp/upload_video.html`
    """
    return render_to_response('upload_video.html')

def view_video(request):
    """
    Directs to view a posted video

    **Template:**

    :template:`myapp/view_video.html`
    """
    return render_to_response('view_video.html')

def view_advice(request):
    """
    Directs to view a posted video

    **Template:**

    :template:`myapp/view_video.html`
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'view_advice.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('view_advice.html')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def time(request):
    """
    Directs to time management homepage

    **Template:**

    :template:`myapp/time.html`
    """
    return render_to_response('time.html')

def rating_form(request):
    """
    Directs to the form for class rating

    **Template:**

    :template:`myapp/rating_form.html`
    """
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

def test(request):
    """
    Directs to the page to where you can choose from classes

    **Template:**

    :template:`myapp/ratings_view.html`
    """
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            class_rated=form.cleaned_data['class_rated']
            class_difficulty_level=form.cleaned_data['class_difficulty_level']
            #print(class_rated,class_difficulty_level,class_hours_spent,rater_grade,class_exams_num,class_hw,class_comments,class_overall);
            #it will go to view rating if successful
            #return HttpResponseRedirect('/ratings_view.html/')
            post.save()
    else:
        form = RateForm()
    return render(request, 'test.html', {'form': form})

def test1(request):
    """
    Directs to view a posted video

    **Template:**

    :template:`myapp/view_video.html`
    """
    rates = Rate.objects.all();
    return render(request, 'test1.html', {'rates': rates})
