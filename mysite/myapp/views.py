from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
    return render_to_response('index.html')

def maps(request):
    return render_to_response('maps.html')

def ratings_landing_page(request):
    return render_to_response('ratings_landing_page.html')
