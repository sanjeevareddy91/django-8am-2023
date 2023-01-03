from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def hello_world(request):
    return HttpResponse("<h1>Hello Welcome to Django Framework!</h1>")


def base_file(request):
    # render -- its for loading the HTML file in django views..
    return render(request,"base.html")


def register(request):
    print(request)
    print(request.POST)
    if request.method == "POST":
        print(request.POST['email'])
        print(request.POST['psw'])
        print(request.POST['psw-repeat'])

    return render(request,'register.html')


def movie_add(request):
    print(request)
    if request.method == "POST":
        # print(request.POST)
        movie_name = request.POST.get('movie_name')
        released_year = request.POST.get('released_year')
        actors = request.POST.get('actors')
        director = request.POST.get('director')
        producer = request.POST.get('producer')
        budget = request.POST.get('budget')
        review = request.POST.get('review')
        print(movie_name)
        check_movie = Movies.objects.filter(movie_name=movie_name)
        if len(check_movie)>0:
            return HttpResponse("Movie Name Already Exist!")
        try:
            Movies.objects.create(movie_name=movie_name,released_year=released_year,actors=actors,director=director,producer=producer,budget=budget,review=review)
            return HttpResponse("Movie Added Successfully!")
        except:
            return HttpResponse("Movie Already Exist!")
    return render(request,'movie_add.html')

def movie_list(request):
    data = Movies.objects.all() # This ORM will fetch the complete data from the Movies model(movies table).
    print(data)
    return render(request,'movie_list.html',{"data":data})

def movie_data(request,id):
    data = Movies.objects.get(id=id)
    print(data)
    return render(request,'movie_data.html',{"data":data})