from django.shortcuts import render

# Create your views here.
def persite(request):
    return render(request, 'home.html')