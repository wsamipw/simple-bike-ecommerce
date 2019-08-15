from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


# Create your models here.


class Bike(models.Model):
    name = models.CharField(default="new bike", max_length=150)
    image = models.ImageField(upload_to='cart/',
                              default='', blank=True, null=True)
    price = models.FloatField(default=0.0)
    date = models.DateTimeField(blank=True, null=True)
    content = RichTextUploadingField(default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cart:bike_view", kwargs={"id": self.id})


class UserCart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="carts", blank=True, null=True)
    bike = models.ForeignKey(Bike, related_name="carts",
                             on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'user Cart'


STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished")
)


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="orders",  on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.TextField(
        max_length=120, choices=STATUS_CHOICES, blank=True, null=True)
    first_name = models.CharField(max_length=120, default="")
    last_name = models.CharField(max_length=120, default="")
    email = models.EmailField("Email", max_length=250,
                              default="")
    address = models.CharField(
        max_length=250, default="")
    city = models.CharField(max_length=120, default="")
    payment_method = models.CharField(
        max_length=250, default="")

    def __str__(self):
        # return self.first_name + ' ' + self.last_name
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="orderItems", on_delete=models.CASCADE, default=None)
    bike = models.ForeignKey(
        Bike, on_delete=models.CASCADE, related_name="orderItems", default=None)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.bike)
