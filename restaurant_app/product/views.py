from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category


def product_list(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    # GET filters
    category = request.GET.get("category")
    spiciness = request.GET.get("spiciness")
    vegetarian = request.GET.get("vegetarian")
    nuts = request.GET.get("nuts")

    if category:
        products = products.filter(category_id=category)

    if spiciness:
        products = products.filter(spiciness=spiciness)

    if vegetarian:
        products = products.filter(vegetarian=True)

    if nuts:
        products = products.filter(contains_nuts=True)

    # PAGINATION
    paginator = Paginator(products, 12)  
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, "product/product_list.html", context)
