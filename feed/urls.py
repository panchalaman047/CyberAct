from django.urls import path
from . import views


urlpatterns = [
    path("main/", views.main_page, name="main-page"),
    path("humanities/",views.humanities,name='humanities'),
    path("education/",views.education,name='education'),
    path('health/',views.health,name='health'),
    path('charity/',views.charity,name='charity'),
    path('religion/',views.religion,name='religion'),
    path('services/',views.services,name='services'),
    path('other/',views.other,name='other'),
    path('environment/',views.environment,name='environment'),
]