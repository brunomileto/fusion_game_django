import datetime
import pprint

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.template import RequestContext


from .forms import SignUpForm, ImageInputForm, EditUserForm, EditProfileForm, EditUserSecurityForm, \
    EditProfileSecurityForm, BankInfoForm

# Create your views here.
from .models import Profile


def logout_view(request):
    logout(request)
    print('passou')
    return redirect('home')


def home_view(request, *args, **kwargs):
    signup_form = SignUpForm()
    login_context = RequestContext(request)
    msg = None
    if request.method == 'POST':
        if request.POST['username']:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(username, password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')

            else:
                return render(request, 'index.html', {'signup_form': signup_form,
                                                      'msg': msg})
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.refresh_from_db()
            user.profile_picture_url = 'another_thing'
            user.save()
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, 'Your profile was successfully updated!')
        else:
            error = signup_form.errors.as_data()
            msg = []
            for key in error:
                for index in range(len(error[key])):
                    validation_error = list(error[key][index])[0]
                    msg.append(validation_error)
            return render(request, 'index.html', {'signup_form': signup_form,
                                                  'msg': msg})
    return render(request, 'index.html', {'signup_form': signup_form,
                                          'msg': msg})


@login_required
def user_profile_view(request, *args, **kwargs):
    current_nav_name = 'Perfil'

    profile_model = request.user.profile
    image_input_form = ImageInputForm()
    edit_user_form = EditUserForm(initial=model_to_dict(profile_model))
    edit_profile_form = EditProfileForm(initial=model_to_dict(profile_model))

    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        edit_profile_form = EditProfileForm(request.POST, instance=request.user.profile)
        image_input_form = ImageInputForm(request.POST, request.FILES)

        if image_input_form.is_valid():
            user = User.objects.get(username=request.user)
            user.profile.profile_picture_url = image_input_form.cleaned_data['profile_picture_url']
            user.save()
        else:
            print(image_input_form.errors)

        if edit_profile_form.is_valid():
            edit_profile_form.save()
        else:
            print(edit_profile_form.errors)

        if request.user.first_name == '' or request.user.first_name is None:
            if request.user.last_name == '' or request.user.last_name is None:
                if edit_user_form.is_valid():
                    edit_user_form.save()
                else:
                    print(edit_user_form.errors)
                    return redirect('settings')
            return redirect('settings')
        return render(request, 'pages/user_profile.html', {'current_nav_name': current_nav_name,
                                                           'form': image_input_form,
                                                           'edit_user_form': edit_user_form,
                                                           'edit_profile_form': edit_profile_form})
    return render(request, 'pages/user_profile.html', {'current_nav_name': current_nav_name,
                                                       'form': image_input_form,
                                                       'edit_user_form': edit_user_form,
                                                       'edit_profile_form': edit_profile_form})


@login_required
def user_profile_settings_view(request, *args, **kwargs):
    current_nav_name = 'Configuracoes'
    current_menu_name = 'Dados Perfil'

    user_model = request.user
    profile_model = request.user.profile
    edit_user_form = EditUserForm()
    edit_profile_form = EditProfileForm()
    print('mare')
    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        edit_profile_form = EditProfileForm(request.POST, instance=request.user.profile)
        print('hare')
        if edit_profile_form.is_valid() and edit_profile_form.is_valid():
            edit_user_form.save()
            edit_profile_form.save()
            print('here')
            return render(request, 'pages/user_profile_settings.html', {'current_nav_name': current_nav_name,
                                                                        'current_menu_name': current_menu_name,
                                                                        'edit_user_form': edit_user_form,
                                                                        'edit_profile_form': edit_profile_form})

        else:
            print(edit_profile_form.errors)
            print(edit_user_form.errors)
    return render(request, 'pages/user_profile_settings.html', {'current_nav_name': current_nav_name,
                                                                'current_menu_name': current_menu_name,
                                                                'edit_user_form': edit_user_form,
                                                                'edit_profile_form': edit_profile_form})


@login_required(redirect_field_name='home')
def user_profile_security_settings_view(request, *args, **kwargs):
    """
    TODO: Ao inserir só o nome ou o só o sobrenome, não é possível inserir o outro que ficou em branco posteriormente
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    current_nav_name = 'Configuracoes'
    current_menu_name = 'Segurança'

    user_model = request.user
    profile_model = request.user.profile
    edit_user_security_form = EditUserSecurityForm(initial=model_to_dict(user_model))
    edit_profile_security_form = EditProfileSecurityForm(initial=model_to_dict(profile_model))
    edit_bank_info_form = BankInfoForm()
    if request.method == 'POST':

        edit_user_security_form = EditUserSecurityForm(request.POST, instance=request.user)
        if edit_user_security_form.is_valid():
            edit_user_security_form.save()
            return redirect('security_settings')
        else:
            print(edit_user_security_form.errors)

        edit_profile_security_form = EditProfileSecurityForm(request.POST, instance=request.user.profile)
        if edit_profile_security_form.is_valid():
            edit_profile_security_form.save()
            return redirect('security_settings')
        else:
            print(edit_profile_security_form.errors)

        edit_bank_info_form = BankInfoForm(request.POST, instance=request.user.profile)
        if edit_bank_info_form.is_valid():
            edit_bank_info_form.save()
            return redirect('security_settings')
        else:
            print(edit_bank_info_form.errors)

    return render(request, 'pages/user_profile_private_settings.html', {'current_nav_name': current_nav_name,
                                                                        'current_menu_name': current_menu_name,
                                                                        'edit_profile_form': edit_profile_security_form,
                                                                        'edit_user_security_form': edit_user_security_form,
                                                                        'edit_bank_info_form': edit_bank_info_form
                                                                        })


@login_required
def user_wallet_view(request, *args, **kwargs):
    current_nav_name = 'Carteira'
    return render(request, 'pages/user_wallet.html', {'current_nav_name': current_nav_name})


