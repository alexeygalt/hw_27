from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models.ad import Ad
from ads.permissions.ad import AuthorAdminModeratorPermission

from ads.serializers.ad import AdSerializer, AdCreateSerializer, AdUpdateSerializer, AdImageSerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat', None)
        cat_query = None

        # filter by category id
        for cat_id in categories:
            if cat_query is None:
                cat_query = Q(category__id__exact=cat_id)
            else:
                cat_query |= Q(category__id__exact=cat_id)
        if cat_query:
            self.queryset = self.queryset.filter(cat_query)

        # filter by ad text
        ad_name = request.GET.get('text', None)
        print(ad_name)
        if ad_name:
            self.queryset = self.queryset.filter(name__icontains=ad_name)

        # filter by user location
        user_location = request.GET.get('location', None)
        if user_location:
            self.queryset = self.queryset.filter(author__location__name__icontains=user_location)

        # Filter by price
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(
                price__range=[price_from, price_to]
            )

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [AuthorAdminModeratorPermission]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [AuthorAdminModeratorPermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AuthorAdminModeratorPermission]


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdImageSerializer
