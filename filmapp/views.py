from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import MovieModelForm,MovieForm,PeopleModelForm
from django.contrib.auth.models import User
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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        data = User(username=username,email=email,is_staff=True)
        data.set_password(password)
        data.save()
        Register_User.objects.create(user_data=data,mobile=mobile)
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
        # poster = request.FILES.get('poster)
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
    print(data.actors.all())
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

def movie_modelform(request):
    form = MovieModelForm()
    print(form)
    # import pdb;pdb.set_trace() # 
    print(request.method)
    if request.method=="POST":
        form = MovieModelForm(request.POST,request.FILES)  # request.FILES -- > for adding the files from the htm.
        # print(form)
        print(request.POST)
        # print(request.FILES)
        if form.is_valid(): # this will validate all the field data is correct or not..
            # actors_info = People.objects.get(id=request.POST['actors'])
            # producers_info = People.objects.get(id=request.POST['producer'])
            # directors_info = People.objects.get(id=request.POST['director'])
            import pdb;pdb.set_trace()
            actors_info = People.objects.filter(id__in=request.POST.getlist('actors'))
            producers_info = People.objects.filter(id__in=request.POST.getlist('producer'))
            directors_info = People.objects.filter(id__in=request.POST.getlist('director'))
            print(actors_info)
            print(producers_info)
            print(directors_info)
            data = form.save(commit=False)
            print(data)
            print(type(data))
            data.save()
            data.actors.add(*actors_info)
            data.producer.add(*producers_info)
            data.director.add(*directors_info)
            data.save()
            return HttpResponse("Model Form Data saved!")
    return render(request,'movie_modelform.html',{'form':form})

def movie_form(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            data = dict(request.POST)
            data.pop('csrfmiddlewaretoken')
            print(request.POST)
            new_data = {ele:data[ele][0] for ele in data}
            Movies.objects.create(**new_data)
            return HttpResponse("Normal Form Data Saved!")
    return render(request,'movie_form.html',{'form':form})

def people_add(request):
    form = PeopleModelForm()
    print(request.method)
    if request.method=="POST":
        form = PeopleModelForm(request.POST,request.FILES)  # request.FILES -- > for adding the files from the htm.
        # print(form)
        # print(request.POST)
        # print(request.FILES)
        if form.is_valid(): # this will validate all the field data is correct or not..
            print(request.POST)
            
            # form.save()
            return HttpResponse("People Model Form Data saved!")
    return render(request,'people_modelform.html',{'form':form})
