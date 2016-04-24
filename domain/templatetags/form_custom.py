from django import template
register = template.Library()
import re

@register.filter('fieldtype')
def fieldtype(field):
    #import ipdb;ipdb.set_trace()
    return field.field.widget.__class__.__name__

@register.filter('req_label')
def req_label(field):
    return field.field.widget.is_required

@register.filter('field_label')
def field_label(field):
    Field_Type = field.field.widget.__class__.__name__
    Field_class = 'input'
    if (Field_Type == 'Select' or Field_Type == 'SelectMultiple'):
        Field_class = 'select'
    elif Field_Type == 'Textarea':
        Field_class =    'textarea'
    elif Field_Type == 'TextInput':
        Field_class =    'input'
    elif Field_Type == 'CheckboxInput':
        Field_class = 'select'
        
    elif Field_Type == 'FileInput':
        Field_class = 'input input-file'
    else:
        Field_class = 'input'

    return Field_class


@register.filter('get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter('get_value')
def get_value(dictionary, key):
    return getattr(dictionary,key)
