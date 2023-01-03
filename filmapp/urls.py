"""FilmIndustry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from filmapp import views

urlpatterns = [
    path('',views.hello_world,name="hello"),
    path('base/',views.base_file,name="base_file"),
    path('register/',views.register),
    path('movie_add/',views.movie_add,name='movie_add'),
    path('movie_list/',views.movie_list,name="movie_list"),
    path('movie_data/<id>',views.movie_data,name="movie_data")

]
