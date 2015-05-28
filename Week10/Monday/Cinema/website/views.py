from django.shortcuts import render
# from django.http import HttpResponse
from .models import Movie


def index(request):
    # return render(request, "index.html")
    movies = Movie.objects.all()

    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html')
