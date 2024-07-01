from django.urls import path
from .views import *
from . import views

app_name="movie"
urlpatterns=[
    path('', views.singer_list_create),
    path('<int:movie_id>', views.singer_detail_update_delete),
    path('<int:movie_id>/song', views.song_read_create),
]