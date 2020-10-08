from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('lemurs/', views.lemurs_index, name='index'),
    path('lemurs/<int:lemur_id>/', views.lemurs_detail, name='detail'),
    path('lemurs/create/', views.LemurCreate.as_view(), name='lemurs_create'),
    path('lemurs/<int:pk>/update/', views.LemurUpdate.as_view(), name='lemurs_update'),
    path('lemurs/<int:pk>/delete/', views.LemurDelete.as_view(), name='lemurs_delete'),
    path('lemurs/<int:lemur_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]