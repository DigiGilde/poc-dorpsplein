import uuid

from django.db.models import CharField, Model, UUIDField
from django.utils.translation import gettext_lazy as _


class Organization(Model):
    id = UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(_("name"), blank=True, max_length=255)

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organizations")
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} ({self.id})"
