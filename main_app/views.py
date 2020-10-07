from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Lemur

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lemurs_index(request):
    lemurs = Lemur.objects.all()
    return render(request, 'lemurs/index.html', { 'lemurs': lemurs })

def lemurs_detail(request, lemur_id):
    lemur = Lemur.objects.get(id=lemur_id)
    return render(request, 'lemurs/detail.html', { 'lemur': lemur })

class LemurCreate(CreateView):
    model = Lemur
    fields = '__all__'