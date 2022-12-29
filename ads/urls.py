from django.urls import path
from rest_framework import routers

from .views.ad import *
from .views.cat import *
from .views.location import LocationViewSet
from .views.selected import SelectionListView, SelectionDetailView, SelectionCreateView, SelectionUpdateView, \
    SelectionDeleteView

loc_router = routers.SimpleRouter()
loc_router.register('location', LocationViewSet)

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
    path("cat/<int:pk>/delete/", CatDeleteView.as_view()),
    path("selection/", SelectionListView.as_view()),
    path("selection/<int:pk>", SelectionDetailView.as_view()),
    path("selection/create/", SelectionCreateView.as_view()),
    path("selection/<int:pk>/update/", SelectionUpdateView.as_view()),
    path("selection/delete/", SelectionDeleteView.as_view()),


]

urlpatterns += loc_router.urls
