from django.contrib import admin
from .models import Order, OrderItem
from django.utils.html import format_html


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    row_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "postal_code",
        "city",
        "paid",
        "created",
        "updated",
    ]
    list_filters = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
