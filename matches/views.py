from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def find_matches_view(request, *args, **kwargs):
    current_nav_name = 'Partidas'
    current_menu_name = 'Procurar Partida'
    print(current_nav_name)
    return render(request, 'pages/find_matches.html', {'current_nav_name': current_nav_name,
                                                       'current_menu_name': current_menu_name
                                                       })


@login_required
def match_creation_view(request, *args, **kwargs):
    current_nav_name = 'Partidas'
    current_menu_name = 'Criar Partida'

    print(current_nav_name)
    return render(request, 'pages/match_creation.html', {'current_nav_name': current_nav_name,
                                                         'current_menu_name': current_menu_name
                                                         })


@login_required
def current_matches_view(request, *args, **kwargs):
    current_nav_name = 'Partidas'
    current_menu_name = 'Minhas Partidas'

    return render(request, 'pages/current_matches.html', {'current_nav_name': current_nav_name,
                                                          'current_menu_name': current_menu_name
                                                          })


@login_required
def match_history_view(request, *args, **kwargs):
    current_nav_name = 'Partidas'
    current_menu_name = 'Historico'

    return render(request, 'pages/match_history.html', {'current_nav_name': current_nav_name,
                                                        'current_menu_name': current_menu_name
                                                        })

