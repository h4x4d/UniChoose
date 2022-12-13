from django.shortcuts import render
from django.views.generic import TemplateView
# TODO: rewrite view according to Alexey templates
from homepage.filters.initial_filter import initial_filter
from homepage.filters.nearest_filter import nearest_filter
from users.models import Preference


class HomepageView(TemplateView):
    template_name = 'homepage/index.html'
    
    def get(self, request):
        user = request.user
        departments = initial_filter(user)

        if user.preference:
            departments = nearest_filter(departments, user)
        else:
            preference = Preference(
                entry_score=310,
                vuz_rating=10.0,
                edu_level=0,
                profile=0,
            )
            preference.save()
            user.preference = preference
            user.save()

        context = {'departments': departments}

        return render(request, self.template_name, context)
