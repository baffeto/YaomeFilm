from django.shortcuts import render
from django.http import JsonResponse
from .models import Film, Actor


def about_film_view(request, id_film):
    """View for film details."""
    film = Film.objects.get(id=id_film)
    return render(request, 'yaome/film.html', {'film': film})

    


# Кнопка search на сайте

def search(request):
    query = request.GET.get('q')
    if query:
        films = Film.objects.filter(title__icontains=query)
    else:
        films = Film.objects.all()
    return render(request, 'yaome/home.html', {'films': films})

def search_ajax(request):
    query = request.GET.get('q')
    if query:
        films = Film.objects.filter(title__icontains=query)
        results = [{'title': film.title} for film in films]
    else:
        results = []
    return JsonResponse(results, safe=False)