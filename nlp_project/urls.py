from django.contrib import admin
from django.urls import path
from . import views
import nltk

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("about/", views.about, name="About page")
]
