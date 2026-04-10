<secure code with environment variables>
import os
from gunicorn import app

if 'GUNICORN_SETTINGS' in os.environ:
  app.config = os.environ['GUNICORN_SETTINGS']
elif 'INSECURE_SITE_SECRET' in os.environ:
  secret_key = os.environ['INSECURE_SITE_SECRET']
  app.config['SECRET_KEY'] = secret_key
