from django import forms

from common.mixins import DisableFormFieldsMixin
from movies.models import Movie


class MovieFormBasic(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['slug']


        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Inception'}),
            "tagline": forms.TextInput(attrs={'placeholder': 'Your mind is the scene of the crime'}),
            "description": forms.Textarea(attrs={'placeholder': 'Description of this movie goes here'}),


        }

class MovieCreateForm(MovieFormBasic):
    ...

class MovieUpdateForm(MovieFormBasic):
    ...

class MovieDeleteForm(DisableFormFieldsMixin, MovieFormBasic):
    ...


class SearchMovieForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )


