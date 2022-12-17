from django.contrib import admin

from ads.models.ad import Ad
from ads.models.category import Category
from ads.models.location import Location

# Register your models here.
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Location)


