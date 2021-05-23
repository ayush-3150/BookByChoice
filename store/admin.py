from django.contrib import admin
from .models import book
from .models import Category, Cart, Order, OrderItem, Payment, BookReview
# Register your models here.


class AdminBook(admin.ModelAdmin):
    list_display = ['name', 'author_name', 'desc', 'price',
                    'category', 'img', 'slug', 'total_Stock', 'available_quantity']
    list_editable = ['slug']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCart(admin.ModelAdmin):
    list_display = ['Book', 'quantity', 'user']


# class AdminOrder(admin.ModelAdmin):
#     list_display = ['order_status', 'payment_method',
#                     'shipping_address', 'phone', 'user', 'total', 'date']

# class BookConfiguration(admin.ModelAdmin):
#     list_display = ['slug']


admin.site.register(book, AdminBook)
admin.site.register(Category, AdminCategory)
admin.site.register(Cart, AdminCart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(BookReview)
