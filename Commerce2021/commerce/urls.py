from django.urls import path
from commerce import views


urlpatterns = [
    path("", views.home, name="home"),
    path("commerce/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("display/", views.display, name="display"),
    #path("log/", views.log_message, name="log"),
]

