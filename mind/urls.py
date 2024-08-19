from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    path('', views.index, name='home'),  
    path('newsletter/<slug:slug>/', views.newsletterin, name='newsletter_detail'),
    path('articlepage/', views.articlepage, name='articlepage'),
    # path('relatedarticle/', views.related_article, name='relatedarticle'),
    path('related_articles/<slug:slug>/', views.related_article, name='related_article'),
    path('articles/category/<slug:slug>/', views.articles_by_category, name='articles_by_category'),
    path('articles<slug:slug>/', views.articles, name='articles'),
    path('category/<slug:slug>/', views.articles, name='articles_by_category'),
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
  