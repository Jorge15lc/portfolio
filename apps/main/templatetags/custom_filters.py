from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def is_empty_richtext(value):
    if not value:
        return True
    soup = BeautifulSoup(value, "html.parser")
    text = soup.get_text(strip=True)
    return not bool(text)