from django.urls import path
from django.conf.urls import url

from . import views
from .views import *


urlpatterns = [
    path('getdata', views.index),
    #path('getstat', stat, name='stat'),
    #path('posts/', views.posts),
    #url(r'^$', HomeView.as_view(), name='home'),
    #url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/week/$', ChartData.as_view()),
    url(r'^api/chart/data/$', ChartData.as_view()),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('post_list/', post_list, name='posts_week'),
    path('post_list/all/', post_all, name='all_url'),
    path('post_list/danger/', post_danger, name='danger_url'),
    path('post_list/success/', post_success, name='success_url'),
    path('post_list/secondary/', post_secondary, name='secondary_url'),
    path('post_list/warning/', post_warning, name='warning_url'),
    path('post_list/<str:category>/', post_category, name='post_category_url'),
]
