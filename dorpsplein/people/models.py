import uuid

from django.conf import settings
from django.db.models import SET_NULL, CharField, Model, OneToOneField, UUIDField
from django.utils.translation import gettext_lazy as _


class People(Model):
    id = UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(_("name"), max_length=255)
    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=SET_NULL, related_name="people", null=True, blank=True)

    class Meta:
        verbose_name = _("people")
        verbose_name_plural = _("people")
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} ({self.id})"

    def small_id(self) -> str:
        return str(self.id)[-8:]
