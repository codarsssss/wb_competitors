from django import template

register = template.Library()


@register.filter(name='divide_by_100')
def divide_by_100(value):
    """Делит значение на 100 и преобразует в целое число."""
    try:
        return int(value) // 100
    except (ValueError, TypeError):
        return 0
