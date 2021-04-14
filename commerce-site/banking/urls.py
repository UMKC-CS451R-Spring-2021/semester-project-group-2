from django.urls import path
from . import views

urlpatterns = [

    path('homepage', views.login, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact')
]