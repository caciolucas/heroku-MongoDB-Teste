from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:id>/<int:like>', views.like, name="like"),
    path('ranking/', views.ranking, name='ranking'),
]
