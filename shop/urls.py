from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("index/", views.index_page, name="index"),
    path("lenta/", views.my_block, name="lenta"),
    path("lenta/<int:id>", views.profile, name="lenta_page"),
    path("form/", views.shop_form, name="form"),
]