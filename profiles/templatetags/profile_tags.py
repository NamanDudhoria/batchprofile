from django import template

register = template.Library()

@register.filter
def split_skills(value, delimiter=','):
    return [skill.strip() for skill in value.split(delimiter)]
