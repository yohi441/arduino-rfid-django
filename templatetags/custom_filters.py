from django import template

register = template.Library()


@register.filter
def dict_key(dictionary, key):
    """Custom template filter to get the value of a dictionary by key."""
    return dictionary.get(key, None)
