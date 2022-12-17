from django.shortcuts import render
from django.views.generic import ListView

from users.models import Account

# TODO: rewrite view according to Alexey templates


class LikedDepartments(ListView):
    # ! Haven't tested this view yet

    template_name = 'departments/index.html'

    def get_queryset(self, account: Account):
        return [rel.department for rel in account.relations.filter(strength=1)]

    def get(self, request):
        context = {
            'liked_departments': self.get_queryset(request.user),
        }
        return render(request, self.template_name, context)
