from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('fill', views.fill_page, name = 'fill'),
    path('confirm', views.confirm_page, name='confirm'),
    path('add', views.add_page, name = 'add'),
    path('review', views.review_page, name = 'review')
]
