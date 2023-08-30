from django.urls import path
from . import views

app_name = 'yaome'

urlpatterns = [
    path('', views.search, name='search'),
    path('film/<id_film>/', views.about_film_view),
    path('search/ajax/', views.search_ajax, name='search_ajax'),
]
