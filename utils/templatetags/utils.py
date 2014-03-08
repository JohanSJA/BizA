from django import template


register = template.Library()


@register.simple_tag
def get_field_verbose_name(instance, field_name):
    """Return verbose_name for a field."""
    return instance._meta.get_field(field_name).verbose_name.title()


@register.simple_tag
def get_field_help_text(instance, field_name):
    '''Return help_text for a field.'''
    return instance._meta.get_field(field_name).help_text
