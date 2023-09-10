from django.contrib import admin , messages
from django .http.request import HttpRequest
from django.db.models import Count, QuerySet
from django.utils.html import format_html , urlencode
from django.urls import reverse


from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value()=='<10':
            return queryset.filter(inventory__lt=10)


@admin.register(models.Produckt)
class ProducktAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
       'slug':['title']
    }
    actions = ['clear_inventory']
    search_fields = ['title']
    list_display = ["title", "unit_price", 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self , produckt):
        return produckt.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, produckt):
        if produckt.inventory < 10:
            return 'Low'
        return "Ok"
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        update_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{update_count} products were succsessfully updated',
            messages.ERROR
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership", 'orders']
    list_editable = ["membership"]
    search_fields = ['first_name', 'last_name']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

    @admin.display(ordering="orders")
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                 'customer__id':customer.id
            }))
        return format_html('<a href="{}">{}</a>', url , customer.orders)
    
    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(orders = Count('order'))


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'produckts_count']
    search_fields = ['title']
    list_per_page = 10 

    @admin.display(ordering='produckts_count')
    def produckts_count(self , collection):
        url = (
            reverse('admin:store_produckt_changelist')
            + '?'
            + urlencode({
                 'collection__id':collection.id
            }))
        return format_html('<a href="{}">{}</a>', url , collection.produckts_count)
               
    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(produckts_count = Count('produckt'))


class OrderItemLine(admin.TabularInline):
    autocomplete_fields= ['produckt']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemLine]
    list_display = ['payment_status', 'placed_at', 'customer_lastname']
    list_per_page = 10

    def customer_lastname(self, order):
        return order.customer.last_name
