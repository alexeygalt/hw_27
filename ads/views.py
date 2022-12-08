import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories, Ads


def index(request):
    return JsonResponse(
        {"status": "ok"}, status=200
    )


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
        response = []
        for item in categories:
            response.append({
                'id': item.id,
                "name": item.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})

    def post(self, request):
        upload_data = json.loads(request.body)
        category = Categories(**upload_data)
        category.save()
        response = {
            'id': category.id,
            'name': category.name
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()
        response = []
        for item in ads:
            response.append({
                'id': item.id,
                "name": item.name,
                "author": item.author,
                "price": item.price
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})

    def post(self, request):
        upload_data = json.loads(request.body)
        ads = Ads.objects.create(**upload_data)
        response = {
            'id': ads.id,
            'name': ads.name,
            'author': ads.author,
            'price': ads.price,
            'description': ads.description,
            'address': ads.address,
            'is_published': ads.is_published
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            'id': category.id,
            'name': category.name
        })


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()
        return JsonResponse({
            'id': ads.id,
            'name': ads.name,
            'author': ads.author,
            'price': ads.price,
            'description': ads.description,
            'address': ads.address,
            'is_published': ads.is_published
        })
