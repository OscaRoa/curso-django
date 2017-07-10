from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    MovieList,
    Movie
)

from .forms import MovieListForm


def hello_world(request):
    """Ejemplo de view que sólo muestra un "Hola mundo" en el navegador."""
    return HttpResponse("Hello world!")


def list_movies(request):
    """View que lista todas las películas en la base de datos."""
    movies = Movie.objects.all().order_by('name')
    context = {
        'movies': movies
    }

    return render(request, 'movies/list.html', context)


def create_movielist(request):
    """View para crear una nueva lista películas por ver."""
    if request.method == "POST":
        form = MovieListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:watchlists")
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'movies/new_watchlist.html', context)
    else:
        form = MovieListForm()
        context = {
            'form': form
        }
        return render(request, 'movies/new_watchlist.html', context)


def list_movielists(request):
    """View que enlista MovieList que hay en la base de datos."""
    lists = MovieList.objects.all().order_by('name')
    context =  {
        'lists': lists
    }

    return render(request, 'movies/list_watchlists.html', context)

def detail_movielist(request, id):
    """View que muestra el detalle de una lista."""
    object = get_object_or_404(MovieList, pk=id)
    context = {
        'list': object
    }

    return render(request, 'movies/detail_watchlist.html', context)

def update_movielist(request, id):
    """View para editar una lista."""
    object = get_object_or_404(MovieList, pk=id)
    if request.method == "POST":
        form = MovieListForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect("movies:watchlists")
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'movies/new_watchlist.html', context)
    else:
        form = MovieListForm(instance=object)
        context = {
            'form': form,
            'list': object
        }
        return render(request, 'movies/new_watchlist.html', context)


def delete_movielist(request, id):
    """View para borrar una lista."""
    object = get_object_or_404(MovieList, pk=id)
    object.delete()

    return redirect("movies:watchlists")
