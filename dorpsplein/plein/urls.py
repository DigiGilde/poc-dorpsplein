from django.urls import path

from .views import PleinView

app_name = "plein"
urlpatterns = [
    path("", PleinView.as_view(), name="index"),
]
