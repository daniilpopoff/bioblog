from django.urls import path
from . import views

urlpatterns =[
    path("about_me/", views.about_me),
    path("heart/", views.heart, name="heart")
]