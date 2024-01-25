# pages/views.py
from django.views.generic import TemplateView
from django import VERSION

class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
    django_ver = VERSION

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["django_version"] = self.django_ver  # Add it to the context
        context['django_ver'] = ".".join(str(i) for i in VERSION)
        return context