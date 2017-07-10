from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^hello/$',
        view=views.hello_world,
        name='hello_world'
    ),

    url(
        regex=r'^peliculas/$',
        view=views.list_movies,
        name='list'
    ),

    url(
        regex=r'^crear-lista/$',
        view=views.create_movielist,
        name='new_watchlist'
    ),

    url(
        regex=r'^listas/$',
        view=views.list_movielists,
        name='watchlists'
    ),

    url(
        regex=r'^listas/(?P<id>\d+)/$',
        view=views.detail_movielist,
        name='detail_watchlist'
    ),

    url(
        regex=r'^editar-lista/(?P<id>\d+)/$',
        view=views.update_movielist,
        name='edit_watchlist'
    ),

    url(
        regex=r'^borrar-lista/(?P<id>\d+)/$',
        view=views.delete_movielist,
        name='delete_watchlist'
    )
]
