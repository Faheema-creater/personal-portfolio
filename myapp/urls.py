from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('education',views.education,name='education'),
    path('skills',views.skills,name='skills'),
    path('achievements',views.achievements,name='achievements'),
    path('experience',views.experience,name='experience'),
    path('contact',views.contact,name='contact')
]