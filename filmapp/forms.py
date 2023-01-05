from django.forms import ModelForm,Form,IntegerField
from .models import Movies
from django import forms

class MovieModelForm(ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"
        # exclude = ('review',) # specific the fieldnames only in tuple format..


class MovieForm(Form):
    movie_name = forms.CharField(max_length=100)
    released_year = forms.IntegerField()
    actors = forms.CharField(max_length=200)
    director = forms.CharField(max_length=50)
    producer = forms.CharField(max_length=50)
    budget = forms.CharField(max_length=10)
    review= forms.CharField()


# crispy-form