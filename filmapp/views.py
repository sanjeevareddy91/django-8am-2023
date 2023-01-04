from django.shortcuts import render,redirect
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

def movie_update(request,id):
    data= Movies.objects.get(id=id)
    print(data)
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        # 1st way to update the data.

        # movie_name = request.POST.get('movie_name')
        # released_year = request.POST.get('released_year')
        # actors = request.POST.get('actors')
        # director = request.POST.get('director')
        # producer = request.POST.get('producer')
        # budget = request.POST.get('budget')
        # review = request.POST.get('review')
        # data.released_year = released_year
        # data.actors = actors
        # data.director = director
        # data.producer = producer
        # data.budget = budget
        # data.review = review
        # data.save()

        # 2nd way to update data
        new_data = dict(request.POST)
        new_data.pop('csrfmiddlewaretoken')
        new_data.pop('movie_name')
        new_data = {ele:new_data[ele][0] for ele in new_data}
        print(new_data)
        Movies.objects.filter(id=id).update(**new_data)
        return redirect('movie_data',id=id)

    return HttpResponse("Updated data!")


def movie_delete(request,id):
    data= Movies.objects.get(id=id)
    data.delete()
    return HttpResponse("Data Deleted Successfully!")