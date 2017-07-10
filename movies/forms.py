from django import forms

from .models import MovieList


class MovieListForm(forms.ModelForm):

    class Meta:
        model = MovieList
        fields = '__all__'
