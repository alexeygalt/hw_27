import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from ads.models.ad import Ad
from ads.models.category import Category
from users.models import User


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list.order_by('-price'), settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        items = []
        for item in page_obj:
            items.append({
                'id': item.id,
                "name": item.name,
                "author_id": str(item.author_id),
                "price": item.price,
                "description": item.description,
                "is_published": item.is_published,
                "image": item.image.url if item.image else None,

            })

        response = {
            'items': items,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        response = {
            'id': ad.id,
            "name": ad.name,
            "author_id": str(ad.author_id),
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ["name", "price", "description", "is_published", "image", "category_id"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data.get('name'),
            price=ad_data.get('price'),
            description=ad_data.get('description'),
            is_published=ad_data.get('is_published'),

        )
        ad.author = get_object_or_404(User, pk=ad_data.get('author_id'))
        ad.category = get_object_or_404(Category, pk=ad_data.get('category_id'))
        ad.save()
        response = {
            'id': ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": str(ad.author),
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,

        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name", "price", "description", "is_published", "image", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)
        ad = self.object

        ad.name = ad_data.get('name')
        ad.author_id = ad_data.get('author_id')
        ad.price = ad_data.get('price')
        ad.description = ad_data.get('description')
        ad.category_id = ad_data.get('category_id')

        ad.save()

        response = {
            'id': ad.id,
            "name": ad.name,
            "author": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url if ad.image else None,

        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ['name', 'image']

    def post(self, request, *args, **kwargs):
        ad = self.get_object()
        ad.image = request.FILES['image']
        ad.save()

        response = {
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": str(ad.author),
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url if ad.image else None
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})
