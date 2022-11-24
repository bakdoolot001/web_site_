from django.contrib import admin
from django.urls import path
# from products.views import index
from . import views


urlpatterns = [
    path("main/", views.index)
]