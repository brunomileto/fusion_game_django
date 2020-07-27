import pprint

from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from matches.forms import MatchCreationForm
from matches.models import Match


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
            # form.save()
            # form.cleaned_data['match_creator'] = request.user.id
            # form.save()
            match = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            match.save()  # Now you can send it to DB
            match.match_creator.add(request.user)

            # match.save()
    else:
        print(form.errors)
        form = MatchCreationForm()

    test = Match.objects.get(id=10)
    print('match_creator = ')
    pprint.pprint(model_to_dict(test))
    a = test.match_creator.all()[0]     # This is a queryset that is essentially a list. This has only one object so I
    # can access it by index 0
    print(a.id)
    b = test.game_name.game_serie
    pprint.pprint(b.game_subcategory.game_category)
    return render(request, 'pages/match_creation.html', {'current_nav_name': current_nav_name,
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
