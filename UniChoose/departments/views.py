from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from users.models import Account

# TODO: rewrite view according to Alexey templates


class LikedDepartments(LoginRequiredMixin, ListView):
    # ! Haven't tested this view yet

    template_name = 'departments/index.html'
    paginate_by = 10

    def get_queryset(self, account: Account):
        return [rel.department for rel in account.relations.filter(strength=1)]

    def get(self, request):
        context = {
            'liked_departments': self.get_queryset(request.user),
        }
        return render(request, self.template_name, context)
