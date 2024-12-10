import os
from django.core.wsgi import get_wsgi_application
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# This checks if the app is running in the Vercel environment
if os.environ.get('VERCEL'):
    from . import app  # Import your app to be used as the handler
    handler = app  # Set 'app' as the handler for Vercel
else:
    application = get_wsgi_application()  # For local or other environments, use the default WSGI application
