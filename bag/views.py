from django.shortcuts import render

def view_bag(request):
    """ A view to render the bag template"""
    return render(request, 'bag/bag.html')
