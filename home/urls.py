from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about,  name='about'),
    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),

]
