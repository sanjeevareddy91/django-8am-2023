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
from django.urls import path,re_path
from filmapp import views

from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Film App",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from rest_framework.authtoken import views as auth_view

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = routers.DefaultRouter()

router.register(r'movieviewset',views.Movieviewset)

urlpatterns = [
    # path('',views.hello_world,name="hello"),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
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
    path('hello_api/',views.hello_api,name='hello_api'),
    path('movie_api/',views.movies_api_view,name="movie_api"),
    path('movie_api_serializer/',views.movies_api_with_serializer,name="movie_api_serializer"),
    path('movie_api_serializer/<pk>',views.movies_api_with_serializer_with_pk,name="movie_api_serializer_with_pk"),
    path('cls_movieapiview/',views.MoviesApiView.as_view(),name="cls_movieapiview"),
    path('cls_movieapiview/<pk>',views.MoviesApiViewWithPK.as_view(),name="cls_movieapiviewpk"),
    path('generic_list/',views.Generic_List.as_view(),name='generic_list'),
    path('generic_create/',views.Generic_Create.as_view(),name='generic_create'),
    path('generic_create_list/',views.Generic_CreateList.as_view(),name='generic_create_list'),
    path('generic_retrieve/<pk>',views.Generic_Retrieve.as_view(),name='generic_retrieve'),
    path('generic_retrieve_update_delete/<pk>',views.Generic_Retrieve_Update_Delete.as_view(),name='generic_retrieve_update_delete'),
    path('create_auth_token/',views.auth_token_create,name="create_auth_token"),
    path('api-auth-token/',auth_view.obtain_auth_token,name="api-auth-token"),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="token_refresh"),
    


]


urlpatterns = urlpatterns + router.urls