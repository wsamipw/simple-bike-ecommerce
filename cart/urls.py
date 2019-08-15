from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('bike/<int:id>', views.bike_view, name='bike_view'),
    path('delete/<int:id>', views.bike_delete, name='bike_delete'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('change_qty/<int:id>', views.change_quantity, name='change_qty'),
    path('checkout/', views.checkout, name='checkout'),
    path('search', views.search, name='search'),
    path('ratings', views.ratings, name='ratings')


]
