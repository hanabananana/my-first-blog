from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    path('pls-news/', views.pls_news, name='pls-news'),
    path('pls-news-map/', views.pls_news_map, name='pls-news-map'),

    # plastic_news.html page
    path('interactive_map/', views.map_create, name='map_create'),
    path('created_map/', views.created_map, name='created_map'),
    path('my_dynamic_map/', views.dynamic_map, name='dynamic_map'),

    # gray vs. orange
    path('interactive_map2/', views.map_create2, name='map_create2'),
    path('created_map2/', views.created_map2, name='created_map2'),
    path('my_dynamic_map2/', views.dynamic_map2, name='dynamic_map2'),

    # red vs. yellow
    path('interactive_map3/', views.map_create3, name='map_create3'),
    path('created_map3/', views.created_map3, name='created_map3'),
    path('my_dynamic_map3/', views.dynamic_map3, name='dynamic_map3'),
]
