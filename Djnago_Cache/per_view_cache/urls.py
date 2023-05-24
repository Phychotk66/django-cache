from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('home/', views.view),
    path('cr/', cache_page(30)(views.course)),
]
