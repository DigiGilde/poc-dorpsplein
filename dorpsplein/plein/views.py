from django.views.generic import TemplateView


class PleinView(TemplateView):
    template_name = "plein/index.html"
