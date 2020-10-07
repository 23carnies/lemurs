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
]