from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(30)
def view(request):
    return render(request, "home.html")

#Template Fragmet Caching
def course(request):
    return render(request, "course.html" )
    
