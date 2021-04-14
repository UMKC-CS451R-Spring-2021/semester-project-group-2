from django.urls import include, path
from commerce import views
from django.contrib import admin


urlpatterns = [
    path("", views.login, name="login"),
    path("commerce/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("transactions/", views.transactions, name="transactions"),
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]