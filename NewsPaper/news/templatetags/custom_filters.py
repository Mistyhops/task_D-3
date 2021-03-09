from django import template

register = template.Library()


@register.filter(name='censor')
def censor(some_str):
    cens_str = ''
    for i in some_str.split():
        cens_str = some_str.replace('ДТП', '@!#$')
    return cens_str
