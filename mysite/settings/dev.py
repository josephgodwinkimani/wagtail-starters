from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "i+i#peh*r379c&6q3ax()#@7q_xn9oo7ujk+o3w^1(4-7haz(n"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAIL_CACHE = False

try:
    from .local import *  # noqa
except ImportError:
    pass
