from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']

    menu_items = MenuItem.objects.filter(parent__isnull=True)
    active_menu_item = None

    for item in menu_items:
        if item.url and request.path.startswith(item.url):
            active_menu_item = item
            break

    context['menu_items'] = menu_items
    context['active_menu_item'] = active_menu_item
    context['menu_name'] = menu_name

    return ''
