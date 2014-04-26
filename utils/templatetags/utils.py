@register.filter
def class_name(value):
    return value.__class__.__name__
