from django import template

register = template.Library()

@register.filter
def array(value, arg):
    return value[arg]