from django.shortcuts import render
from products.models import Product, Category


def index(request):
    """ A view to return the index page """
    webshop_news_products = Product.objects.filter(category__name="webshop_news")

    context = {
        'products': webshop_news_products,
    }

    return render(request, 'home/index.html', context)
