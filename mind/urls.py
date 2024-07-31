from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  
    path('newsletter/', views.newsletter, name='newsletter'),  
    path('articles/', views.articles, name='articles'),  
    path('registration/', views.register, name='register'),  
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),
    path('find_element/', views.multi_step_form, name='find_element'),
    path('result/', views.result, name='result'),

]
