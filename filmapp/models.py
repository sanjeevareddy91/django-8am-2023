from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_name = models.CharField(max_length=100,unique=True)
    released_year = models.PositiveIntegerField()
    actors = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    budget = models.CharField(max_length=10)
    review= models.TextField()


    def __str__(self):
        return self.movie_name

    class Meta:
        db_table = 'movies'
# create table movies(movie_name varchar(20))