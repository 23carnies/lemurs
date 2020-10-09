from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Lemur, Feeding, Toy, Photo
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = '23carnies'

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
    toys_lemur_doesnt_have = Toy.objects.exclude(id__in = lemur.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'lemurs/detail.html', {
        'lemur': lemur, 'feeding_form': feeding_form, 'toys': toys_lemur_doesnt_have 
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
    fields = ['name', 'species', 'description', 'age']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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

def add_photo(request, lemur_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to lemur_id or lemur (if you have a lemur object)
            photo = Photo(url=url, lemur_id=lemur_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', lemur_id=lemur_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)