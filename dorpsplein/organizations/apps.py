from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrganizationConfig(AppConfig):
    name = "dorpsplein.organizations"
    verbose_name = _("Organizations")
