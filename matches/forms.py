from django import forms
from matches.models import Match, Platform, Game


class MatchCreationForm(forms.ModelForm):
    game_name = forms.ModelChoiceField(queryset=Game.objects.all(), empty_label="Escolha o Jogo: ")
    platform = forms.ModelChoiceField(queryset=Platform.objects.all(), empty_label='Escolha a plataforma: ')

    class Meta:
        model = Match
        fields = ['game_name', 'platform', 'match_comment', 'bet_value', 'game_rules', 'game_mode']


