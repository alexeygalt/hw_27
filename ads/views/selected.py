from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ads.models.selected import Selected
from ads.permissions.selected import SelectedByOwner
from ads.serializers.selected import SelectionSerializer, SelectionCreateSerializer, SelectionUpdateSerializer


class SelectionListView(generics.ListAPIView):
    queryset = Selected.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(generics.RetrieveAPIView):
    queryset = Selected.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(generics.CreateAPIView):
    queryset = Selected.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(generics.UpdateAPIView):
    queryset = Selected.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, SelectedByOwner]


class SelectionDeleteView(generics.DestroyAPIView):
    queryset = Selected.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectedByOwner]
