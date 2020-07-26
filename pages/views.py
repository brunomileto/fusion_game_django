from django.shortcuts import render


# # Create your views here.
# def home_view(request, *args, **kwargs):
#     form =
#     return render(request, 'index.html', {})


def components_view(request, *args, **kwargs):
    return render(request, 'components.html', {})


def register_view(request, *args, **kwargs):
    return render(request, 'reset_password.html', {})


def checkout_view(request, *args, **kwargs):
    return render(request, 'checkout.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def cart_view(request, *args, **kwargs):
    return render(request, 'cart.html', {})


def error_404_view(request, *args, **kwargs):
    return render(request, '404.html', {})


def match_view(request, *args, **kwargs):
    return render(request, 'match-2.html', {})


def matches_list_view(request, *args, **kwargs):
    return render(request, 'matches-list.html', {})


def store_view(request, *args, **kwargs):
    return render(request, 'store-2.html', {})


def user_activity_view(request, *args, **kwargs):
    return render(request, 'users-activity.html', {})


def user_view(request, *args, **kwargs):
    return render(request, 'user-profile.html', {})


def user_settings_view(request, *args, **kwargs):
    return render(request, 'users-settings.html', {})


def widgets_view(request, *args, **kwargs):
    return render(request, 'widgets.html', {})


def base_view(request, *args, **kwargs):
    return render(request, 'base.html', {})
