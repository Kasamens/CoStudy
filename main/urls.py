from django.urls import path
from . import views
from .models import Post

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(thought = Post), name='index'),
]