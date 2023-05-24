from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
def Api(request):
    nm = cache.get('name', 'has_enpired')
    if nm == 'has_expired':
        cache.set('name', 'Anaya noor', 30)
        nm = cache.get('name')
    return render(request, 'home.html', {'fm':nm})