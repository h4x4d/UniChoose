from django.shortcuts import render
from django.views.generic import ListView

from users.models import Account

# TODO: rewrite view according to Alexey templates


class LikedUniversities(ListView):
    # ! Haven't tested this view yet

    template_name = 'universities/index.html'

    def get_queryset(self, account: Account):
        return account.liked_unis.all()

    def get(self, request):
        context = {
            'liked_universities': self.get_queryset(request.user),
        }

        render(request, self.template_name, context)
