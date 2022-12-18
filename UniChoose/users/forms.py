from django import forms
from django.contrib.auth.forms import UserChangeForm
from users.models import Account
from fixtures.region_choice_field_fixture import region_choices
from django.core.validators import MaxValueValidator, MinValueValidator


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username',)

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

    class Meta():
        model = Account
        fields = ('username', )
        exclude = ('password', )

        widgets = {

        }


class SubjectsSelectionForm(forms.Form):
    region = forms.ChoiceField(
        choices=region_choices, required=True, label='Ваш регион')
    mark_informatics = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Информатика'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_math = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Математика'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_russian = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Русский язык'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_social = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Обществознание'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_foreign = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Иностранный язык'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_biology = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Биология'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_geography = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'География'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_chemistry = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Химия'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_physics = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Физика'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_literature = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Литература'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_history = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'История'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mark_additional = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Доп. баллы'}),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
