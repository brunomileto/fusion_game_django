from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
from matches.forms import MatchCreationForm


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
    form = MatchCreationForm()
    if request.method == 'POST':
        form = MatchCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('hey')
    else:
        print(form.errors)
        form = MatchCreationForm()

    print(current_nav_name)
    return render(request, 'pages/formtest.html', {'current_nav_name': current_nav_name,
                                                   'current_menu_name': current_menu_name,
                                                   'form': form,
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

