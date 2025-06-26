from django import template

register = template.Library()

@register.simple_tag
def is_active(request, path):
    return 'active' if request.path == path else ''
