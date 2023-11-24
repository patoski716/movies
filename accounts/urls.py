from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('details/<str:slug>/', views.details,name="details"),
    path('fdetails/<str:slug>/', views.fdetails,name="fdetails"),

    # path('contact/', views.contact, name='contact'),
]