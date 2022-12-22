from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'about/index.html'
