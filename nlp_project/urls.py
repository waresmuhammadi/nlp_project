from django.contrib import admin
from django.urls import path
from . import views
import nltk

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="About page"),
    path("get-data/",views.get_details, name="Getting and parsing data")
]
