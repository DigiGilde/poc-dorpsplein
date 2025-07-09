from .base import *  # noqa: F403
from .base import TEMPLATES, env

# GENERAL
# ----------------------------------------------------------------------------------------------------------------------
DEBUG = False
SECRET_KEY = env.str(
    "DJANGO_SECRET_KEY",
    default="django-insecure-nxdIgqzFUCMJcAzs8WWx2SjsoWDM0A434MbhJb9obSDQqDv3GTcz7CMxuUsbbAHc",
)

# TEST CONFIG
# ----------------------------------------------------------------------------------------------------------------------
# To speed up tests, we use a fast password hasher
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
TEMPLATES[0]["OPTIONS"]["debug"] = True
