"""fusion_games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from users.views import home_view, logout_view, user_profile_view, user_profile_settings_view, user_wallet_view, \
    user_profile_security_settings_view
from pages.views import match_view, checkout_view, contact_view, cart_view, store_view, \
    error_404_view, matches_list_view, components_view, widgets_view, base_view, user_view
from matches.views import find_matches_view, current_matches_view, match_history_view, match_creation_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),

    path('home/', user_profile_view, name='user_profile'),
    path('configurações_perfil/', user_profile_settings_view, name='settings'),
    path('configurações_seguranca/', user_profile_security_settings_view, name='security_settings'),
    path('carteira/', user_wallet_view, name='user_wallet'),

    path('procurar_partidas/', find_matches_view, name='find_matches'),
    path('minhas_partidas/', current_matches_view, name='current_matches'),
    path('historico_partidas/', match_history_view, name='match_history'),
    path('criar_partida/', match_creation_view, name='match_creation'),

    path('carrinho/', cart_view),
    path('loja/', store_view),
    path('base/', base_view),
    path('partida-2/', match_view),
    path('lista_partidas/', matches_list_view),
    path('perfil/', user_profile_view),
    path('erro_404/', error_404_view),
    path('checkout/', checkout_view),
    path('contato/', contact_view),
    path('componentes/', components_view),
    path('widgets/', widgets_view),
    path('user-profile/', user_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
