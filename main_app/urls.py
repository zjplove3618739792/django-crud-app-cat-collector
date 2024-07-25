from django.urls import path
from .views import CatCreate, CatUpdate, CatDelete
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path('cats/create/', CatCreate.as_view(), name='cat-create'),
    path('cats/<int:pk>/update/', CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', CatDelete.as_view(), name='cat-delete'),
]


