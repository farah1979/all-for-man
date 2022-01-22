from django.shortcuts import render
from .models import Newsletters
from .forms import NewslettersForm


def newsletters(request):
    """ A view render all newsletters from superusers to page"""
    newsletter = Newsletters.objects.all()

    template = 'newsletters/newsletters.html'
    context = {
        'newsletter': newsletter,
    }

    return render(request, template, context)
