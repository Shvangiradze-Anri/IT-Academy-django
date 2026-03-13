from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from product.models import Product


def cart(request):

    cart_items = Cart.objects.all()

    subtotal = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        "cart_items": cart_items,
        "subtotal": subtotal
    }

    return render(request, "cart/cart_list.html", context)


def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    item, created = Cart.objects.get_or_create(product=product)

    if not created:
        item.quantity += 1
        item.save()

    return redirect(request.META.get("HTTP_REFERER"))


def increase_quantity(request, cart_id):

    item = Cart.objects.get(id=cart_id)
    item.quantity += 1
    item.save()

    return redirect("cart")


def decrease_quantity(request, cart_id):

    item = Cart.objects.get(id=cart_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    return redirect("cart")


def delete_cart(request, cart_id):

    item = Cart.objects.get(id=cart_id)
    item.delete()

    return redirect("cart")