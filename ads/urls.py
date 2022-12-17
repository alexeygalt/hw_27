from django.urls import path
from .views.ad import *
from .views.cat import *

urlpatterns = [

    path("ad/", AdListView.as_view()),
    path("ad/<int:pk>/", AdDetailView.as_view()),
    path("ad/create/", AdCreateView.as_view()),
    path("ad/<int:pk>/update/", AdUpdateView.as_view()),
    path("ad/<int:pk>/delete/", AdDeleteView.as_view()),
    path("ad/<int:pk>/upload_image/", AdImageView.as_view()),
    path("cat/", CatListView.as_view()),
    path("cat/<int:pk>", CatDetailView.as_view()),
    path("cat/create/", CatCreateView.as_view()),
    path("cat/<int:pk>/update/", CatUpdateView.as_view()),
    path("cat/<int:pk>/delete/", CatDeleteView.as_view()),


]
