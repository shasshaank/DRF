from django.contrib import admin
from api.models import OrderItem, Order

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inline = [
        OrderItemInline
    ]

admin.site.register(Order,OrderAdmin)