from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, View

from fixtures.regions_fixture import regions
from users.forms import EditProfileForm, SignUpForm, SubjectsSelectionForm
from users.models import Account, Subject
from universities.models import Region
from fixtures.subjects_attrs import subjects_attr_names

# ! These are not finished probably


class SignUpFormView(FormView):
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('homepage:home')
    form_class = SignUpForm

    def form_valid(self, form):
        user = Account.objects.create_user(**form.cleaned_data)
        login(self.request, user)
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, View):
    model = Account
    template_name = 'auth/profile.html'

    def get(self, request):
        context = {
            'username':
            request.user.username,
            'disliked_dpts_count':
            request.user.relations.filter(strength=-1).count(),
            'liked_dpts_count':
            request.user.relations.filter(strength=1).count(),
        }

        return render(request, self.template_name, context=context)


class EditProfileView(LoginRequiredMixin, FormView):
    template_name = 'auth/profile_edit.html'
    success_url = reverse_lazy('auth:profile')
    form_class = EditProfileForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.request.user})
        return kwargs


class SelectSubjectsView(View):
    template_name = 'auth/select_subjects.html'  # ! Update the template
    success_url = reverse_lazy('auth:login')

    def get(self, request):
        if request.user.is_authenticated:
            self.success_url = reverse_lazy('auth:profile')

        subject_form_initial = {
            'region': request.user.region.name,
            'max_distance': request.user.max_distance,
        }

        for name in subjects_attr_names:
            try:
                subject_form_initial[name] = Subject.objects.get(
                    account_id=request.user.id,
                    name=name,
                ).mark
            except Exception:
                pass

        form = SubjectsSelectionForm(initial=subject_form_initial)

        context = {
            'form': form,
            'regions': regions,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        account = Account.objects.filter(id=request.user.id)
        account.update(max_distance=request.POST.get('max_distance'))

        try:
            account.update(region=Region.objects.get(
                name=request.POST.get('region')))
        except Exception:
            pass

        inputted_marks = {}
        for name in subjects_attr_names:
            if request.POST.get(name) != '':
                inputted_marks[name] = request.POST.get(name)

        for key in inputted_marks:
            Subject.objects.update_or_create(
                account_id=request.user.id,
                name=key,
                defaults={
                    'account': request.user,
                    'name': key,
                    'mark': inputted_marks[key],
                })

        return redirect('auth:profile')
