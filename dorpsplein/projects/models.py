import uuid_utils.compat as uuid
from django.db.models import CASCADE, CharField, ForeignKey, ManyToManyField, Model, UUIDField
from django.utils.translation import gettext_lazy as _


class Project(Model):
    id = UUIDField("ID", primary_key=True, default=uuid.uuid7, editable=False)
    name = CharField(_("name"), blank=True, max_length=255)

    team = ManyToManyField("people.People", related_name="projects", blank=True)
    organization = ForeignKey("organizations.Organization", on_delete=CASCADE, related_name="projects")

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("Projects")
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} ({self.id})"

    @property
    def small_id(self) -> str:
        return str(self.id)[-8:]
