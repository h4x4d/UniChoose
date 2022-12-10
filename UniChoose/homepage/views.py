from django.shortcuts import render


def home(request):
    template = 'homepage/index.html'
    return render(request, template)
