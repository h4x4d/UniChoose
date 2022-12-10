from django.views.generic import ListView
from django.shortcuts import render
from users.models import Account

# TODO: rewrite view according to Alexey templates


class LikedDepartments(ListView):
    # ! Haven't tested this view yet

    template_name = 'departments/index.html'

    def get_queryset(self, account: Account):
        return account.liked_dpts.all()

    def get(self, request):
        context = {
            'liked_departments': self.get_queryset(request.user),
        }

        render(request, self.template_name, context)
