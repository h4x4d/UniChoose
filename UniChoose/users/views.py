from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, View

from fixtures.subjects_attrs import (reversed_subjects_convert,
                                     subjects_attr_names, subjects_convert)
from universities.models import Region
from users.forms import EditProfileForm, SignUpForm, SubjectsSelectionForm
from users.models import Account, AccountDepartmentRelations, Subject

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


class SelectSubjectsView(FormView):
    template_name = 'auth/select_subjects.html'
    success_url = reverse_lazy('auth:edit_info')
    form_class = SubjectsSelectionForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['max_distance'] = self.request.user.max_distance

        for subject in self.request.user.subjects.all():
            kwargs['initial'][subjects_convert[subject.name]] = subject.mark

        kwargs.update({'instance': self.request.user})
        try:
            kwargs.update({'region_value': self.request.user.region.name})
        except AttributeError:
            pass

        return kwargs

    def post(self, request):
        if self.form_valid(request):
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
                name=reversed_subjects_convert[key],
                defaults={
                    'account': request.user,
                    'name': reversed_subjects_convert[key],
                    'mark': inputted_marks[key],
                })

        return redirect('auth:edit_info')

    # ! might need to be rewritten to show form errors to user


def delete_liked_departments(request):
    AccountDepartmentRelations.objects.filter(
        account_id=request.user.id).delete()
    return redirect('auth:profile')


def delete_recommendation_profile(request):
    account = Account.objects.get(id=request.user.id)

    account.preference.entry_score = 310
    account.preference.vuz_rating = 10.0
    account.preference.edu_level = 0
    account.preference.profile = 0

    account.preference.save()

    return redirect('auth:profile')
