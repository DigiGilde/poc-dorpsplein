import socket

from .base import *  # noqa: F403
from .base import INSTALLED_APPS, env

# GENERAL
# ----------------------------------------------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = env.str(
    "DJANGO_SECRET_KEY",
    default="django-insecure-7Osdh5bY7SPLKDhMqeDjhtAwSoyJ7kGWwQ6XVAFC05P5UmQwqMl3F9emKQ37QPcu",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]  # noqa: S104
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"] + [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# CACHES
# ----------------------------------------------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# EMAIL
# ----------------------------------------------------------------------------------------------------------------------
EMAIL_HOST = env.str("EMAIL_HOST", default="mailpit")
EMAIL_PORT = 1025

# django-extensions
# ----------------------------------------------------------------------------------------------------------------------
INSTALLED_APPS += ["django_extensions"]
