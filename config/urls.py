from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include("dorpsplein.plein.urls")),
    path("personen/", include("dorpsplein.people.urls")),
    path("projecten/", include("dorpsplein.projects.urls")),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()

    # This allows the error pages to be debugged during development
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
