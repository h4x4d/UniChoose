from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.validators import MaxValueValidator, MinValueValidator

from fixtures.regions_fixture import regions_choice
from fixtures.subjects_attrs import (subjects_attr_names,
                                     subjects_attr_placeholders)
from users.models import Account
from users.validators import (validate_distance, validate_region,
                              validate_subject)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, **kwargs):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()

        return user


# * idk what to do right now as of 11.12, have no clue what the design of
# * profile page will look like
class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = Account
        fields = ('username', )
        exclude = ('password', )

        labels = {
            'username': 'Имя',
        }


class SubjectsSelectionForm(forms.Form):

    def __init__(self, **kwargs):
        super().__init__()
        if 'region_value' in kwargs:
            self.fields['region'].widget.attrs['value'] = kwargs[
                'region_value']

        for name, placeholder in zip(subjects_attr_names,
                                     subjects_attr_placeholders):
            self.fields[name] = forms.IntegerField(
                widget=forms.NumberInput(attrs={'placeholder': placeholder}),
                validators=[
                    MinValueValidator(0),
                    MaxValueValidator(100),
                    validate_subject,
                ],
                required=False)

        initial = kwargs['initial']

        for field in initial:
            self.fields[field].initial = initial[field]

    region = forms.ChoiceField(choices=regions_choice,
                               validators=[validate_region])
    region.initial = 'Выберите регион...'
    region.widget.template_name = 'widgets/datalist.html'
    region.widget.attrs = {
        'class': 'form-control',
        'placeholder': 'Выберите регион...',
    }
    max_distance = forms.IntegerField(min_value=0,
                                      max_value=10000,
                                      validators=[validate_distance])
    max_distance.widget.attrs = {'placeholder': 'Максимальное расстояние'}
