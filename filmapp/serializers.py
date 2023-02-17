from rest_framework import serializers
from .models import *





class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors = PeopleSerializer(read_only=True, many=True)
    director = PeopleSerializer(read_only=True, many=True)
    producer = PeopleSerializer(read_only=True, many=True)
    class Meta:
        model = Movies
        fields = ('movie_name','released_year','actors','producer','director','budget','review','poster')
        # exclude = ('actors','producer','director')