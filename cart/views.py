from django.shortcuts import render, get_object_or_404
import time
# from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User, auth

from django.urls import reverse
from django.http import HttpResponse
from .forms import OrderItemForm, UserCartForm, OrderForm
from django.contrib import messages
from cart.models import Bike, Order, OrderItem, UserCart
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from django.db.models import FloatField
from django.db.models import Count
from django.shortcuts import redirect
from django.db.models import Q

# Create your views here.


def bike_view(request, id=None):
    bike = Bike.objects.get(id=id)
    context = {
        'bike': bike
    }
    return render(request, 'cart/bike.html', context)


@login_required(login_url='/admin/login/')
def add_to_cart(request):
    carts = UserCart.objects.filter(user=request.user)
    if request.method == 'POST':
        form = UserCartForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.quantity = 1
            form = new_form
            form.save()
            messages.success(
                request, 'You have successfully added your items in cart')
        else:
            messages.error(request, 'Error adding to cart')
    context = {
        'carts': carts
    }
    return render(request, 'cart/add_to_cart.html', context)


def change_quantity(request, id=None):
    instance = get_object_or_404(UserCart, id=id)
    if request.method == 'POST':
        instance.quantity = request.POST['quantity']
        instance.save()

    return redirect('/cart/add_to_cart/')


def bike_delete(request, id=None):
    obj = get_object_or_404(UserCart, id=id)
    print(obj.id)
    obj.delete()
    return redirect('/cart/add_to_cart/')


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Bike.objects.filter(Q(name__icontains=srch) |
                                        (Q(price__icontains=srch))
                                        )
            if match:
                return render(request, 'cart/search.html', {'sr': match})
            else:
                messages.error(request, 'no result found')
        else:
            return redirect('cart/search/')
    return render(request, 'cart/search.html')


def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.status = "Started"
            form = new_form
            form.save()
            cart_items = UserCart.objects.filter(user=request.user)
            for item in cart_items:
                i = OrderItem(order=form, bike=item.bike,
                              quantity=item.quantity)
                i.save()
                item.delete()
    context = {
        # "form": form,
        # "forms": forms
    }
    return render(request, 'cart/checkout.html', context)


def ratings(request):
    return render(request, 'cart/ratings.html')
