from django.views.generic import DetailView, ListView

from .models import People


class PeopleListView(ListView):
    model = People
    context_object_name = "people"
    template_name = "people/people_list.html"


class PeopleDetailView(DetailView):
    model = People
    context_object_name = "person"
    template_name = "people/people_detail.html"
