from django.contrib import admin

from .models import (
    MovieList,
    Movie,
    Tag,
    Studio,
    Director
)

admin.site.register(MovieList)
admin.site.register(Movie)
admin.site.register(Tag)
admin.site.register(Studio)
admin.site.register(Director)
