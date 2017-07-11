from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)
from django.urls import reverse_lazy

from .models import (
    Movie,
    MovieList
)

from .forms import MovieListForm


class ListMovies(ListView):
    """View que lista las películas en la base de datos."""

    queryset = Movie.objects.all()
    template_name = "movies/list.html"
    context_object_name = "movies"


class CreateMovielist(CreateView):
    """View que crea una nueva watchlist."""

    model = MovieList
    form_class = MovieListForm
    template_name = "movies/new_watchlist.html"
    success_url = reverse_lazy("movies:watchlists")


class ListMovielist(ListView):
    """View que lista las watchlists creadas."""

    queryset = MovieList.objects.all()
    template_name = "movies/list_watchlists.html"
    context_object_name = "lists"


class UpdateMovielist(UpdateView):
    """View que edita una watchlist."""

    model = MovieList
    pk_url_kwarg = "id"
    form_class = MovieListForm
    success_url = reverse_lazy("movies:watchlists")
    template_name = "movies/new_watchlist.html"


class DetailMovielist(DetailView):
    """View que muestra el detalle de una lista."""

    model = MovieList
    pk_url_kwarg = "id"
    context_object_name = "list"
    template_name = "movies/detail_watchlist.html"


class DeleteMovielist(DeleteView):
    """View para borrar una watchlist."""

    model = MovieList
    pk_url_kwarg = "id"
    context_object_name = "list"
    template_name = "movies/delete_watchlist.html"
    success_url = reverse_lazy("movies:watchlists")
