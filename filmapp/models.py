from django.db import models

from django.contrib.auth.models import User 
# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=25)
    dob = models.DateTimeField()
    image = models.ImageField(upload_to='peoples',null=True,blank=True)

    def __str__(self):
        return self.name

class Movies(models.Model):
    movie_name = models.CharField(max_length=100,unique=True)
    released_year = models.PositiveIntegerField()
    actors = models.ManyToManyField(People)
    director = models.ManyToManyField(People,related_name='directors_info')
    producer = models.ManyToManyField(People,related_name='producers_info')
    budget = models.CharField(max_length=10)
    review= models.TextField()
    poster = models.ImageField(upload_to='posters',null=True,blank=True)

    def __str__(self):
        return self.movie_name

    class Meta:
        db_table = 'movies'
# create table movies(movie_name varchar(20))

class Register_User(models.Model):
    user_data = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.user_data.username

    class Meta:
        db_table = 'register_user'
