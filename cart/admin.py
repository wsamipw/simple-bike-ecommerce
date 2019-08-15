from django.contrib import admin
from .models import Bike, Order, OrderItem, UserCart
from django.utils.html import format_html


class BikeModelAdmin(admin.ModelAdmin):
    list_display = ["__str__",
                    "image", "date", "content"]
    list_display_links = ["__str__"]
    list_filter = ["date"]

    class Meta:
        model = Bike


class UserCartModelAdmin(admin.ModelAdmin):
    list_display = ["user", "bike", 'quantity', 'timestamp']
    list_display_links = ["user"]
    list_filter = ['bike', 'user', 'timestamp']

    class Meta:
        model = UserCart


class OrderModelAdmin(admin.ModelAdmin):

    def items(self):
        i = ''
        order_items = self.orderItems.all()
        for item in order_items:
            i += '<a href="/admin/cart/orderitem/%d">%s</a>' % (
                (item.id), str(item.bike))
            if not order_items.last() == item:
                i += ', '
        return format_html(i)
    items.allow_tags = True

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    list_display = ["__str__", "user", full_name,
                    "email", "city", "status", items, "timestamp"]
    list_display_links = ["__str__"]
    list_filter = ['timestamp']

    class Meta:
        model = Order


class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "order", "bike", "quantity"]
    list_display_links = ["__str__"]
    list_filter = ['order']

    class Meta:
        model = OrderItem


admin.site.site_header = 'BikeHub Administration'
admin.site.register(Bike, BikeModelAdmin)
admin.site.register(Order, OrderModelAdmin)
admin.site.register(OrderItem, OrderItemModelAdmin)
admin.site.register(UserCart, UserCartModelAdmin)
