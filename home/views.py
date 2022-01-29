from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to render the home page with all
    newest products has been added to store"""
    webshop_news_products = Product.objects.filter(
                    category__name="webshop_news")

    context = {
        'products': webshop_news_products,
    }

    return render(request, 'home/index.html', context)
