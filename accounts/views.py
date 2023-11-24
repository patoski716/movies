from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.
def home(request):
    queryset=Features.objects.all()
    items_per_page = 3
    # Create a Paginator object
    paginator = Paginator(queryset, items_per_page)
    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')
    try:
        # Get the Page object for the given page number
        items = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        items = paginator.page(1)
    except EmptyPage:
        # If the page parameter is out of range, show the last page
        items = paginator.page(paginator.num_pages)

    queryset=Movie.objects.all()
    context={"items":items,"queryset":queryset}
    return render(request,'home.html',context)

def fdetails(request,slug):
    queryset =get_object_or_404(Features, slug=slug)
    context={"queryset":queryset}
    return render(request,'fdetails.html',context)

def movies(request):
    queryset=Movie.objects.all()
    context={"queryset":queryset}
    return render(request,'movies.html',context)

def details(request,slug):
    queryset = get_object_or_404(Movie, slug=slug)
    context={"queryset":queryset}
    return render(request,'details.html',context)