from django.contrib import admin
from .models import Product
# Register your models here.
admin.site.site_header='Mangopi'
admin.site.register(Product)