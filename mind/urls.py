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
    path('privacy/', views.privacy, name='privacy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('statedc/', views.statedc, name='statedc'),
    path('linkpolicy/', views.linkpolicy, name='linkpolicy'),
    path('yyrequired/', views.yyrequired, name='yyrequired'),
    path('yystore/', views.yystore, name='yystore'),
    path('team/', views.team, name='team'),
    path('articlepage/', views.articlepage, name='articlepage'),
    path('how_we_work/', views.howwework, name='howwework'),
]
  