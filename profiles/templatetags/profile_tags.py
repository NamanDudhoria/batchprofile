from django import template

register = template.Library()

@register.filter(name='split_skills')
def split_skills(value):
    if value:
        return [skill.strip() for skill in value.split(',')]
    return []
