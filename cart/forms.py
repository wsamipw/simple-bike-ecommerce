from django import forms

from .models import UserCart, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'status', 'first_name', 'last_name',
                  'email', 'address', 'city', 'payment_method']


class OrderItemForm(forms.ModelForm):
    class Meta:
        fields = ['bike_id', 'order_id', 'quantity', 'price']


class UserCartForm(forms.ModelForm):
    class Meta:
        model = UserCart
        fields = ['user', 'bike', 'quantity']
