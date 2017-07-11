from django.conf.urls import url

from . import class_based_views as views

urlpatterns = [
    url(
        regex=r'^peliculas/$',
        view=views.ListMovies.as_view(),
        name='list'
    ),

    url(
        regex=r'^crear-lista/$',
        view=views.CreateMovielist.as_view(),
        name='new_watchlist'
    ),

    url(
        regex=r'^listas/$',
        view=views.ListMovielist.as_view(),
        name='watchlists'
    ),

    url(
        regex=r'^listas/(?P<id>\d+)/$',
        view=views.DetailMovielist.as_view(),
        name='detail_watchlist'
    ),

    url(
        regex=r'^editar-lista/(?P<id>\d+)/$',
        view=views.UpdateMovielist.as_view(),
        name='edit_watchlist'
    ),

    url(
        regex=r'^borrar-lista/(?P<id>\d+)/$',
        view=views.DeleteMovielist.as_view(),
        name='delete_watchlist'
    )
]
