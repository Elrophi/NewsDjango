from django.urls import path
from . import views

urlpatterns=[
    path('', views.news_today, name='newsToday'),
    path('search/', views.search_results, name='search_results'),
    path('archives/<str:past_date>/', views.past_days_news, name='pastNews')
]