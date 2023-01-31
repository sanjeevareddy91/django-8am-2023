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
    # path('',views.hello_world,name="hello"),
    path('base/',views.base_file,name="base_file"),
    path('',views.register,name="register"),
    path('movie_add/',views.movie_add,name='movie_add'),
    path('movie_list/',views.movie_list,name="movie_list"),
    path('movie_data/<id>',views.movie_data,name="movie_data"),
    path('movie_update/<id>',views.movie_update,name="movie_update"),
    path('movie_delete/<id>',views.movie_delete,name="movie_delete"),
    path('movie_modelform/',views.movie_modelform,name='movie_modelform'),
    path('movie_form/',views.movie_form,name='movie_form'),
    path('people_add/',views.people_add,name="people_add"),
    path('login',views.login_user,name="login_user"),
    path('user_details/<id>',views.user_data,name="user_data"),
    path('logout/',views.logout_user,name="logout_user"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('verify_otp/',views.verify_otp,name="verify_otp"),
    path('changes_password/<id>',views.change_password,name="change_password"),
    path('cls_hello/',views.HelloClassView.as_view(),name="cls_hello"),
    path('cls_register/',views.RegisterUserView.as_view(),name='cls_register'),
    path('cls_register_list/',views.RegisterUserListView.as_view(),name="cls_register_list"),
    path('cls_register_detail/<pk>/',views.RegisterUserDetailView.as_view(),name="cls_register_detail"),
    path('cls_register_update/<pk>/',views.RegisterUserUpdateView.as_view(),name="cls_register_update"),
    path('hello_api/',views.hello_api,name='hello_api')

]
