from django.contrib import admin
from models import ProductA

class ProductAAdmin(admin.ModelAdmin):
  list_display = ('id', 'name_kr','name_en', 'maker_code', 'created', 'updated')

admin.site.register(ProductA, ProductAAdmin)
