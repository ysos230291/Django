from django.contrib import admin
from .models import Product

# ahora queremos que donde aparecen los productos me muestre no solo el nombre 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','short_description','stock',)  # lo que muestras en la tabla 
    search_fields = ('name', 'short_description',)        # buscador
    list_filter = ('name',)                               # barra de filtrado a la derecha
    date_hierarchy = ('discount_until')                   # barra de filtrado arriba 

admin.site.register(Product,ProductAdmin)
