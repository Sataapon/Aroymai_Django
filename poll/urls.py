from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('fill', views.fill_page, name = 'fill'),
    path('add', views.add_page, name = 'add'),
    path('review', views.review_page, name = 'review'),
    path('about', views.about_page, name = 'about')
]
