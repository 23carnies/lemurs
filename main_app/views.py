from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Lemur, Feeding, Toy
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'lemurs/detail.html', {
        'lemur': lemur, 'feeding_form': feeding_form 
        })

def add_feeding(request, lemur_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.lemur_id = lemur_id
        new_feeding.save()
    return redirect('detail', lemur_id=lemur_id)

class LemurCreate(CreateView):
    model = Lemur
    fields = '__all__'

class LemurUpdate(UpdateView):
    model = Lemur
    fields = ['species', 'description', 'age']

class LemurDelete(DeleteView):
    model = Lemur
    success_url = '/lemurs/'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request, lemur_id, toy_id):
    Lemur.objects.get(id=lemur_id).toys.add(toy_id)
    return redirect('detail', lemur_id=lemur_id)