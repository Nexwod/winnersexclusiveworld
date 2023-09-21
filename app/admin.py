from django.contrib import admin
from . models import Product, Customer, Cart, Payment, OrderPlaced, Payapp
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'producer', 'product_image', ]

@admin.register(Customer)   
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'mobile', 'state' ]

@admin.register(OrderPlaced)   
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity', 'ordered_date', 'status', 'payments' ]
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def payments(self, obj):
        link = reverse("admin:app_payapp_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.receipt)

@admin.register(Payment)   
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'payment_image', 'paid' ]

@admin.register(Cart)   
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity' ]
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


@admin.register(Payapp)   
class PayappModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'contact', 'address', 'state', 'receipt', 'amount', 'paid','payment_time' ]