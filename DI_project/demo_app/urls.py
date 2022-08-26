from django.urls import path
from demo_app import views

urlpatterns = [
    path("Confucianism", views.confucianism_detail, name="confucianism"),
    path("Taoism", views.taoism_detail, name="taosim")
]
