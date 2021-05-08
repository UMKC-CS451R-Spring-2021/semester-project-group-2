from django.urls import path
from . import views

urlpatterns = [

    path('homepage/login/', views.homepage, name='homepage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('notifications/', views.notifications, name='notifications'),
]