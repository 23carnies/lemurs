from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('lemurs/', views.lemurs_index, name='index'),
    path('lemurs/<int:lemur_id>/', views.lemurs_detail, name='detail'),
]