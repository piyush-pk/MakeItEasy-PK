from django import template

register = template.Library()

# @register.simple_tag
# @register.filter
def index(indexable, i):
    return indexable[i]

def typeof(var):
    return type(var)

def strcontains(sourse, str):
    return str.contains(sourse)

register.filter('index', index)
register.filter('typeof', typeof)