from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from users.forms import EditProfileForm, SignUpForm
from users.models import Account

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
            'username': request.user.username,
            'liked_unis_count': request.user.liked_unis.all().count(),
            'liked_dpts_count': request.user.liked_dpts.all().count(),
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
    template_name = 'INSERT TEMPLATE'
    success_url = reverse_lazy('auth:login')
    
    def get(self, request):
        if request.user.is_authenticated:
            self.success_url = reverse_lazy('auth:profile')
            
        
