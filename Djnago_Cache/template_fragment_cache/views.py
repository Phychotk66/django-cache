from django.shortcuts import render

# Create your views here.
def tmp(requset):
    return render(requset, "home.html")