from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ register calculate function for subtotal in shoppong bag"""

    return price * quantity
