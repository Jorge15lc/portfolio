from django.http import HttpResponse
from django.conf import settings
import os

def robots_txt(request):
    # Ruta al archivo robots.txt en tu carpeta de static
    filepath = os.path.join(settings.BASE_DIR, 'static/robots.txt')
    with open(filepath, 'r') as f:
        content = f.read()
    return HttpResponse(content, content_type="text/plain")