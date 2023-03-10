from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from .models import *
from .forms import MovieModelForm,MovieForm,PeopleModelForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# import sendgrid
import os
# from sendgrid.helpers.mail import Mail, Email, To, Content
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import random
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import json
from .serializers import MovieSerializer
from rest_framework.authtoken.models import Token
# from filmapp.models import do_stuff

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
        # data = User(username=username,email=email,is_staff=True)
        # data.set_password(password)
        # data.save()
        # Register_User.objects.create(user_data=data,mobile=mobile)

        # import pdb;pdb.set_trace()
        # send_mail(subject='Registration Confirmation',message="Thanks for the registration. You are successfully registered in Filmindustry application.",from_email='sanjeevasimply@gmail.com',recipient_list=[email])
        messages.success(request,'Registration is successful and email sent')
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
            # import pdb;pdb.set_trace()
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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_check = authenticate(username=username,password=password)
        if user_check:
            login(request,user_check)
            messages.success(request,user_check.username+" Logged In successfully")
            return redirect('user_data',user_check.id)
        else:
            messages.error(request,"Invalid credentials")
    return render(request,'login.html')

def user_data(request,id):
    id_info = User.objects.get(id=id)
    data = Register_User.objects.get(user_data=id_info)
    return render(request,'user_data.html',{'data':data})

def logout_user(request):
    # print(request.user)
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('login_user')

def forgot_password(request):
    if request.method == "POST":
        email = request.POST['email']
        user_data = User.objects.filter(email=email)
        print(user_data)
        if user_data:
            otp = str(random.randint(1000,9999999))
            data = Register_User.objects.get(user_data=user_data.first())
            print(data)
            data.otp = otp
            data.save()
            message = "Please use the below OTP for changing the password. {}".format(otp)
            send_mail(subject='OTP verification',message=message,from_email='gsanjeevreddy91@gmail.com',recipient_list=[email])
            messages.success(request,'Verification OTP has been sent to your email id.')
            return redirect('verify_otp')
        else:
            messages.error(request,'Email id doenot exist!')
    return render(request,'forgot_password.html')

def verify_otp(request):
    if request.method == "POST":
        otp = request.POST['otp']
        otp_data = Register_User.objects.filter(otp=otp)
        if otp_data:
            messages.success(request,'OTP verified successfully,Please change your password!')
            return redirect('change_password',id=otp_data.first().user_data.id)
        else:
            messages.error(request,'Invalid OTP')
    return render(request,'verify_otp.html')

def change_password(request,id):
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request,'Both passwords are not matching')
            return redirect('change_password',id=id)
        data = User.objects.get(id=id)
        data.set_password(password)
        data.save()
        messages.success(request,'Password Changed Successfully')
        return redirect('login_user')
    return render(request,'change_password.html')


# class based views


# get -- 
# post --
# put -- 
# delete --
class HelloClassView(View):
    def get(self,request):
        return HttpResponse("Hello Classed Based View")


# Generic View..
class RegisterUserView(CreateView):
    model = Register_User
    fields = "__all__"
    success_url = reverse_lazy('cls_hello')  # Reverse_lazy this help you to redirect to respective URL after the successful request..


class RegisterUserListView(ListView):
    model = Register_User


class RegisterUserDetailView(DetailView):
    model = Register_User

class RegisterUserUpdateView(UpdateView):
    model = Register_User
    fields = "__all__"
    success_url = reverse_lazy('cls_hello')

# CreateListDetailUpdateDeleteView


# Django Restframework Apis:::::

# Function Based Apis..


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PUT','DELETE'])
def hello_api(request):
    dummy_data = {
        "sanjeeva":{
            "mobile":884783783,
            "email" : "gsanjeevreddy19@gmail.com"
        },
        "rajesh":{
            "mobile":903930333,
            "email":'rajesh@gmail.com'
        }
    }
    if request.method == "GET":
        return Response({"message":"Hello World"})
    elif request.method == "POST":
        data = request.data
        email = "gsanjeevreddy91@gmail.com"
        password = "356227727"
        if data.get('email') == email and data.get('password') == password:
            return Response({
                "name" : "sanjeeva",
                "message" : "Logged In"
            })
        else:
            return Response({
                "message" : "Invalid Credentials"
            })
    elif request.method == "DELETE":
        print(request.data)
        dummy_data.pop(request.data.get('name'))
        return Response({
            "message":"Deleted SucessFully",
            "data":dummy_data
        })

@api_view(['GET','POST','PUT',"DELETE"])
def movies_api_view(request):
    if request.method == "GET":
        all_movies = list(Movies.objects.all().values())
        # import pdb;pdb.set_trace()
        return Response({"movies":all_movies})
    elif request.method == "POST":
        print(request)
        new_data = request.data.get('data')
        converted_data = json.loads(new_data)
        print(converted_data.get('movie_name'))
        # import pdb;pdb.set_trace()
        if (converted_data.get('movie_name') == None) or ('movie_name' in converted_data and converted_data.get('movie_name') == ''):
            return Response({
                "message" : "movie_name is required field"
            }) 
        # print(request.data)
        actor_info = [People.objects.get(id=converted_data['actors'])]
        director_info = [People.objects.get(id=converted_data['director'])]
        producer_info = [People.objects.get(id=converted_data['producer'])]
        converted_data['poster'] = request.data['poster']
        movie_data = Movies(movie_name=converted_data['movie_name'],poster=converted_data['poster'],released_year=converted_data['released_year'],budget=converted_data['budget'],review=converted_data['review'])
        movie_data.save()
        movie_data.actors.add(*actor_info)
        movie_data.director.add(*director_info)
        movie_data.producer.add(*producer_info)
        movie_data.save()
        # import pdb;pdb.set_trace()
        converted_data['poster'] = request.data['poster'].name
        # print(converted_data)
        # print(dir(request.data['poster']))
        # print(request.data['poster'].name)
        return Response(converted_data)
    elif request.method == "PUT":
        print(request.data)
        new_data = request.data.get('data')
        converted_data = json.loads(new_data)
        actor_info = [People.objects.get(id=converted_data['actors'])]
        director_info = [People.objects.get(id=converted_data['director'])]
        producer_info = [People.objects.get(id=converted_data['producer'])]
        converted_data['poster'] = request.data['poster']
        movie_data = Movies.objects.get(id=converted_data['id'])
        movie_data.poster.delete(True) # delete the previous poster assigned t the record from the file path..
        movie_data.movie_name = converted_data['movie_name']
        movie_data.released_year = converted_data['released_year']
        movie_data.budget = converted_data['budget']
        movie_data.review = converted_data['review']
        movie_data.poster = converted_data['poster']
        movie_data.save()
        movie_data.actors.add(*actor_info)
        movie_data.director.add(*director_info)
        movie_data.producer.add(*producer_info)
        movie_data.save()
        converted_data['poster'] = request.data['poster'].name
        return Response(converted_data)

    elif request.method == "DELETE":
        print(request.data)
        new_data = request.data.get('id')
        Movies.objects.get(id=new_data).delete()
        return Response({
            "message" :"Deleted Successfully"
        })

@api_view(['GET','POST'])
def movies_api_with_serializer(request):
    if request.method == "GET":
        all_movies = Movies.objects.all()
        print(all_movies)
        serializer = MovieSerializer(all_movies,many=True)
        print(serializer.data)
        # import pdb;pdb.set_trace()
        return Response({"movies":serializer.data})

    elif request.method == "POST":
        print(request.data)
        new_data = request.data.get('data')
        converted_data = json.loads(new_data)
        converted_data['poster'] = request.data['poster']
        print(converted_data)
        serializer = MovieSerializer(data=converted_data)
        print(serializer)
        if serializer.is_valid():
            data = serializer.save()
            actor_info = [People.objects.get(id=converted_data['actors'])]
            director_info = [People.objects.get(id=converted_data['director'])]
            producer_info = [People.objects.get(id=converted_data['producer'])]
            data.actors.add(*actor_info)
            data.producer.add(*producer_info)
            data.director.add(*director_info)
            data.save()
            return Response({
                "message" : "Movie Added"
            })
        else:
            return Response({
                "message" : "Validate the data"
            })


@api_view(["GET","PUT","DELETE"])
def movies_api_with_serializer_with_pk(request,pk):
    try:
        movies_data = Movies.objects.get(pk=pk)
    except:
        return Response({
            "message" : "Record doesnot exist"
        })

    if request.method == "GET":
        # print(request.data)
        # movies_data = Movies.objects.get(pk=pk)
        # print(movies_data)
        serializer = MovieSerializer(movies_data)
        return Response({
            "movie" : serializer.data
        })
    elif request.method == "PUT":
        print(request.data)
        new_data = request.data.get('data')
        converted_data = json.loads(new_data)
        converted_data['poster'] = request.data['poster']
        print(converted_data)
        serializer = MovieSerializer(movies_data,data=converted_data)
        print(serializer)
        if serializer.is_valid():
            data = serializer.save()
            actor_info = [People.objects.get(id=converted_data['actors'])]
            director_info = [People.objects.get(id=converted_data['director'])]
            producer_info = [People.objects.get(id=converted_data['producer'])]
            data.actors.add(*actor_info)
            data.producer.add(*producer_info)
            data.director.add(*director_info)
            data.save()
            return Response({
                "message" : "Movie Updated"
            })
        else:
            return Response({
                "message" : "Validate the data"
            })

    elif request.method == "DELETE":
        movies_data.delete()
        return Response({
            "message":"Movie Delete successfully"
        })


# Class Based APIS():
    # These are segregated into 3 types again:
    #     1) Classbased apis(APIView)
    #     2) Generic Api Views()
    #     3) Viewsets

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

class MoviesApiView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self,request):
        import pdb;pdb.set_trace()
        all_movies = Movies.objects.all()
        serializer = MovieSerializer(all_movies,many=True)
        # import pdb;pdb.set_trace()
        return Response({"movies":serializer.data})

    def post(self,request):
        print(request.data)
        new_data = request.data.get('data')
        converted_data = json.loads(new_data)
        converted_data['poster'] = request.data['poster']
        print(converted_data)
        serializer = MovieSerializer(data=converted_data)
        print(serializer)
        if serializer.is_valid():
            data = serializer.save()
            actor_info = [People.objects.get(id=converted_data['actors'])]
            director_info = [People.objects.get(id=converted_data['director'])]
            producer_info = [People.objects.get(id=converted_data['producer'])]
            data.actors.add(*actor_info)
            data.producer.add(*producer_info)
            data.director.add(*director_info)
            data.save()
            return Response({
                "message" : "Movie Added"
            })
        else:
            return Response({
                "message" : "Validate the data"
            })

class MoviesApiViewWithPK(APIView):

    def get_object(self,pk):
        try:
            # import pdb;pdb.set_trace()
            all_movies = Movies.objects.get(pk=pk)
            return {"data":all_movies}
        except:
            return {
                "message":"record doesnot exist"
            }
    def get(self,request,pk):
        movies_data = self.get_object(pk)
        # import pdb;pdb.set_trace()
        if movies_data.get('message'):
            return Response({"message":movies_data.get('message')})
        serializer = MovieSerializer(movies_data['data'])
        return Response({"movies":serializer.data})

    def put(self,request,pk):
        print(request.data)
        movies_data = self.get_object(pk)
        new_data = request.data.get('data')
        converted_data = json.loads(new_data)
        converted_data['poster'] = request.data['poster']
        print(converted_data)
        serializer = MovieSerializer(movies_data,data=converted_data)
        print(serializer)
        if serializer.is_valid():
            data = serializer.save()
            actor_info = [People.objects.get(id=converted_data['actors'])]
            director_info = [People.objects.get(id=converted_data['director'])]
            producer_info = [People.objects.get(id=converted_data['producer'])]
            data.actors.add(*actor_info)
            data.producer.add(*producer_info)
            data.director.add(*director_info)
            data.save()
            return Response({
                "message" : "Movie Updated"
            })
        else:
            return Response({
                "message" : "Validate the data"
            })

    def delete(self,request,pk):
        movies_data = self.get_object(pk)
        movies_data.delete()
        return Response({
            "message":"Movie Delete successfully"
        })


# Generic APIView..

from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView 


class Generic_List(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class Generic_Create(CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def create(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        data = request.data
        actor_info = [People.objects.get(id=data.pop('actors'))]
        producer_info = [People.objects.get(id=data.pop('producer'))]
        director_info = [People.objects.get(id=data.pop('director'))]
        movie_data = Movies.objects.create(**data)
        movie_data.actors.add(*actor_info)
        movie_data.producer.add(*producer_info)
        movie_data.director.add(*director_info)
        movie_data.save()
        return Response({
            "Message":"Movie Saved"
        })

class Generic_List(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class Generic_CreateList(ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def create(self,request,*args,**kwargs):
        data = request.data
        actor_info = [People.objects.get(id=data.pop('actors'))]
        producer_info = [People.objects.get(id=data.pop('producer'))]
        director_info = [People.objects.get(id=data.pop('director'))]
        movie_data = Movies.objects.create(**data)
        movie_data.actors.add(*actor_info)
        movie_data.producer.add(*producer_info)
        movie_data.director.add(*director_info)
        movie_data.save()
        return Response({
            "Message":"Movie Saved"
        })

class Generic_Retrieve(RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class Generic_Retrieve_Update_Delete(RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def update(self,request,*args,**kwargs):
        data = request.data
        actor_info = [People.objects.get(id=data.pop('actors'))]
        producer_info = [People.objects.get(id=data.pop('producer'))]
        director_info = [People.objects.get(id=data.pop('director'))]
        new_data = Movies.objects.filter(id=kwargs['pk'])
        movie_data = new_data.update(**data)
        new_data[0].actors.add(*actor_info)
        new_data[0].producer.add(*producer_info)
        new_data[0].director.add(*director_info)
        new_data[0].save()
        return Response({
            "Message":"Movie Updated"
        })


# Django Viewsets

from rest_framework import viewsets 

class Movieviewset(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def create(self,request,*args,**kwargs):
        data = request.data
        actor_info = [People.objects.get(id=data.pop('actors'))]
        producer_info = [People.objects.get(id=data.pop('producer'))]
        director_info = [People.objects.get(id=data.pop('director'))]
        movie_data = Movies.objects.create(**data)
        movie_data.actors.add(*actor_info)
        movie_data.producer.add(*producer_info)
        movie_data.director.add(*director_info)
        movie_data.save()
        return Response({
            "Message":"Movie Saved"
        })


@api_view(['POST'])
def auth_token_create (request):
    if request.method == "POST":
        print(request.data)
        user_check = authenticate(username=request.data['username'],password=request.data['password'])
        if user_check:
            token_data = Token.objects.create(user=user_check)

            return Response({
                "message":"Token Generated Successfully",
                'token':token_data.key
            })
        else:
            return Response({
                "message":"Invalid credentials"
            })
