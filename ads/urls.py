from django.urls import path
from .views import *

urlpatterns = [

    path("", index),
    path("cat/", CategoriesView.as_view()),
    path("ad/", AdsView.as_view()),
    path("cat/<int:pk>/", CategoriesDetailView.as_view()),
    path("ad/<int:pk>/", AdsDetailView.as_view()),
]
