from django import template

register = template.Library()

@register.filter
def incr(val):
	return val+1