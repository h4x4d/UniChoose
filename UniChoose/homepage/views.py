from django.views.generic import TemplateView

# TODO: rewrite view according to Alexey templates


class HomepageView(TemplateView):
    template_name = 'homepage/index.html'
