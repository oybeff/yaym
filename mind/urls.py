from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('yaym/', views.about, name='about')
]