import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
# TODO: rewrite view according to Alexey templates
from homepage.filters.initial_filter import initial_filter


class HomepageView(TemplateView):
    template_name = 'homepage/index.html'

    def get(self, request):
        t = datetime.datetime.now()
        context = {
            'universities': len(initial_filter(request.user)),
            'time': str(datetime.datetime.now() - t),
        }

        return render(request, self.template_name, context)
