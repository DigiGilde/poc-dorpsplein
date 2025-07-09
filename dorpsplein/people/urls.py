from django.urls import path

from .views import PeopleDetailView, PeopleListView

app_name = "people"
urlpatterns = [
    path("", PeopleListView.as_view(), name="list"),
    path("<str:pk>/", PeopleDetailView.as_view(), name="detail"),
]
