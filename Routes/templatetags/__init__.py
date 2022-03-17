from django import template

register = template.Library()

@register.filter
def array_value(value,arg):
    return value[arg]