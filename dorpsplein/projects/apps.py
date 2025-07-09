from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProjectConfig(AppConfig):
    name = "dorpsplein.projects"
    verbose_name = _("Projects")
