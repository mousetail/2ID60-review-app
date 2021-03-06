from django import template

register = template.Library()

@register.filter
def yearStudent(value, arg):
    '''returns the year the student is in in ranks'''
    diff = value - arg
    rtn = ""
    if diff == 0:
        rtn = "1st"
    elif diff == 1:
        rtn = "2nd"
    elif diff == 2:
        rtn = str(diff) + "rd"
    elif diff > 2:
        rtn = str(diff) + "th"
    else:
        rtn = "ERROR"
    return rtn
