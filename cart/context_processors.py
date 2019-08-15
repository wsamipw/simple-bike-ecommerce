from cart.models import UserCart


def cart_count(request):
    cart_count = UserCart.objects.filter(user=request.user).count()
    return {
        'cart_count': cart_count
    }
