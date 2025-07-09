import uuid
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, UUIDField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    id = UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(_("name"), blank=True, max_length=255)
    email = EmailField(_("email address"), unique=True)

    # Ensure these fields from AbstractUser are not used
    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.id})
