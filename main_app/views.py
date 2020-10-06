from django.shortcuts import render
from django.http import HttpResponse

class Lemur:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age

lemurs = [
    Lemur('Zoboomafoo', 'ring-tailed', 'precocious', 4),
    Lemur('Jovian', 'ring-tailed', 'shy', 10),
    
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Wow! Lemurs!</h1>')

def about(request):
    return render(request, 'about.html')

def lemurs_index(request):
    return render(request, 'lemurs/index.html', { 'lemurs': lemurs })