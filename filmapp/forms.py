from django.forms import ModelForm,Form,IntegerField
from .models import Movies,People
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class MovieModelForm(ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"
        exclude = ('actors','director','producer') # specific the fieldnames only in tuple format..
        # fields = ('movie_name','actors','released_year','director','producer','budget','review')

    actors = forms.ModelMultipleChoiceField(
        queryset = People.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    director = forms.ModelMultipleChoiceField(
        queryset = People.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    producer = forms.ModelMultipleChoiceField(
        queryset = People.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )


class MovieForm(Form):
    movie_name = forms.CharField(max_length=100)
    released_year = forms.IntegerField()
    actors = forms.CharField(max_length=200)
    director = forms.CharField(max_length=50)
    producer = forms.CharField(max_length=50)
    budget = forms.CharField(max_length=10)
    review= forms.CharField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('movie_name', css_class='form-group col-md-6 mb-0'),
                Column('released_year', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('actors', css_class='form-group col-md-6 mb-0'),
                Column('director', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('producer', css_class='form-group col-md-6 mb-0'),
                Column('budget', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('review', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )
# crispy-form


class PeopleModelForm(ModelForm):
    class Meta:
        model = People
        fields = "__all__"
        # exclude = ('review',) # specific the fieldnames only in tuple format..
