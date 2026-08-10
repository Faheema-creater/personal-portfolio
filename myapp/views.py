from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def education(request):
    return render(request,'education.html')

def skills(request):
    return render(request,'skills.html')

def achievements(request):
    return render(request,'achievements.html')

def experience(request):
    return render(request,'experience.html')


def contact(request):
    return render(request,'contact.html')