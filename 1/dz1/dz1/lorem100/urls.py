from django.urls import path
from . import views

urlpatterns = [
    path('lorem/', views.lorems, name="lorem"),
]
