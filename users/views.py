import json

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models.location import Location
from users.models import User


# Create your views here.

class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        users = (self
                 .object_list
                 .annotate(is_published=Count('ad', filter=Q(ad__is_published=True)))
                 .select_related('location')
                 )
        paginator = Paginator(users, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        users_on_page = paginator.get_page(page_number)

        user_list = []
        for user in users_on_page:
            user_list.append(
                {
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "age": user.age,
                    "locations": str(user.location),
                    "is_published": user.is_published

                }
            )
        response = {
            "items": user_list,
            "total": paginator.count,
            "number_of_pages": paginator.num_pages
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        response = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "locations": str(user.location)
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'role', 'password', 'age', 'location']

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user = User.objects.create(
            username=user_data.get('username'),
            password=user_data.get('password'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            role=user_data.get('role'),
            age=user_data.get('age')
        )
        location, _ = Location.objects.get_or_create(name=user_data.get('locations'))
        user.location = location
        user.save()

        response = {

            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "locations": str(user.location)

        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'role', 'password', 'age', 'location']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)
        user = self.object
        user.username = user_data.get('username')
        user.password = user_data.get('password')
        user.first_name = user_data.get('first_name')
        user.last_name = user_data.get('last_name')
        user.age = user_data.get('age')

        location, _ = Location.objects.get_or_create(name=user_data.get('locations'))
        user.location = location
        user.save()

        response = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "locations": str(user.location)

        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': "ok"}, status=200)
