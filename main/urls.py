from django.urls import path
from . import views


urlpatterns = [
    path("", views.starting_page, name="stating-page"),
    path("signuporganization/",views.organization,name="organization")
]