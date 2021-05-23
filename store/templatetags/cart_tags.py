from django import template
from math import floor

register = template.Library()

@register.simple_tag
def multiply(a , b ):
    return a*b

@register.filter
def cal_total_payable_amount(cart):
    total=0
    for c in cart:
        b=c.get('book')
        price=c.get('book').price
        total_of_single_book=price * c.get('quantity')
        total= total + total_of_single_book
    return total
