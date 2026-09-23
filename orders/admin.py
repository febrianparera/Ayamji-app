from django.contrib import admin
from .models import Customer, Product, ProductRequest, RequestItem


class RequestItemInline(admin.TabularInline):
    model = RequestItem
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('nama', 'telepon', 'created_at')
    search_fields = ('nama', 'telepon')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nama', 'unit', 'harga', 'is_nugget')
    list_filter = ('unit', 'is_nugget')
    search_fields = ('nama',)


@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('kode', 'customer', 'marketing', 'status', 'created_at')
    list_filter = ('status', 'source')
    search_fields = ('kode', 'customer__nama')
    inlines = [RequestItemInline]