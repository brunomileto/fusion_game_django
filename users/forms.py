from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ImageField, DateField, TextInput

from users.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class ImageInputForm(forms.ModelForm):
    profile_picture_url = ImageField(label='Imagem do Perfil',
                                     widget=forms.FileInput(attrs={'class': 'inputfile inputfile-1'}))

    class Meta:
        model = Profile
        fields = ['profile_picture_url']


class EditProfileForm(forms.ModelForm):
    birth_date = DateField(label='',
                           required=False,
                           widget=forms.DateInput(attrs={'data-type': 'datepicker',
                                                         'type': 'date',
                                                         'date': 'yyyy-mm-dd',
                                                         'data-datepicker': 'true',
                                                         }))
    cpf = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    xbox_gametag = forms.CharField(required=False)
    psn_gametag = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['phone', 'birth_date', 'xbox_gametag', 'psn_gametag', 'cpf']


class EditProfileSecurityForm(forms.ModelForm):
    birth_date = DateField(required=False, label='',
                           widget=forms.DateInput(attrs={'data-type': 'datepicker',
                                                         'type': 'date',
                                                         'date': 'yyyy-mm-dd',
                                                         'data-datepicker': 'true',
                                                         }))
    cpf = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['cpf', 'birth_date']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class EditUserSecurityForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class BankInfoForm(forms.ModelForm):
    # bank_name = forms.CharField(required=False)
    # bank_account = forms.CharField(required=False)
    # bank_agency = forms.CharField(required=False)
    # bank_digit = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['bank_name', 'bank_account', 'bank_agency', 'bank_digit']
