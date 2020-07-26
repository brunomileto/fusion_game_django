from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from datetime import date
from users.models import User

# Create your models here.


class GameCategory(models.Model):
    game_category = models.CharField(max_length=240, blank=False, null=False, unique=True)

    def __str__(self):
        return self.game_category


class GameSubCategory(models.Model):
    game_subcategory = models.CharField(max_length=240, blank=False, null=False, unique=True)
    game_category = models.ForeignKey(GameCategory, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.game_subcategory


class GameSerie(models.Model):
    game_series = models.CharField(max_length=240, blank=False, null=False, unique=True)
    game_subcategory = models.ForeignKey(GameSubCategory, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.game_series


class Platform(models.Model):
    platform_name = models.CharField(max_length=240, blank=False, null=False, unique=True)

    def __str__(self):
        return self.platform_name


class Game(models.Model):
    game_name = models.CharField(max_length=240, blank=False, null=False, unique=True)
    game_serie = models.ForeignKey(GameSerie, on_delete=models.CASCADE, blank=False, null=False)
    platform = models.ManyToManyField(Platform)

    def __str__(self):
        return self.game_name.__str__()


class GameRule(models.Model):
    rule_01 = models.CharField(max_length=240, blank=True, null=True, default=None)
    rule_02 = models.CharField(max_length=240, blank=True, null=True, default=None)
    rule_03 = models.CharField(max_length=240, blank=True, null=True, default=None)
    game_name = models.ForeignKey(Game, on_delete=models.CASCADE, blank=False, null=False, unique=True)

    def __str__(self):
        return self.game_name.__str__()


class GameMode(models.Model):
    game_mode_01 = models.CharField(max_length=240, blank=True, null=True, default=None)
    game_mode_02 = models.CharField(max_length=240, blank=True, null=True, default=None)
    game_mode_03 = models.CharField(max_length=240, blank=True, null=True, default=None)
    game_mode_04 = models.CharField(max_length=240, blank=True, null=True, default=None)
    game_name = models.ForeignKey(Game, on_delete=models.CASCADE, blank=False, null=False, unique=True)

    def __str__(self):
        return self.game_name.__str__()


class Match(models.Model):
    WIN = 'WIN'
    DRAW = 'DRAW'
    LOSE = 'LOSE'
    RESULTS_CHOICE = [
        (None, 'Informe o resultado da partida: '),
        (WIN, 'Ganhei'),
        (DRAW, 'Empatamos'),
        (LOSE, 'Perdi'),
    ]
    game_name = models.ForeignKey(Game, on_delete=models.CASCADE, blank=False, null=False)
    match_creation_date = models.DateField(blank=False, null=False, default=date.today)
    match_end_date = models.DateField(blank=True, null=True, default=None)
    match_status = models.CharField(max_length=120, blank=False, null=False, default='created')
    match_comment = models.CharField(max_length=480, blank=True, null=False)
    bet_value = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False,
                                    validators=[MinValueValidator(Decimal('10.00'))])
    mc_result = models.CharField(max_length=24, blank=True, null=False, default='', choices=RESULTS_CHOICE)
    mc_main_statistic = models.CharField(max_length=120, blank=True, null=True, default='')
    mc_opp_main_statistic = models.CharField(max_length=120, blank=True, null=True, default='')
    mc_print = models.ImageField(upload_to='matches_results/', blank=True, null=True, default=None)
    opp_result = models.CharField(max_length=24, blank=True, null=True, default='', choices=RESULTS_CHOICE)
    opp_main_statistic = models.CharField(max_length=120, blank=True, null=True, default='')
    opp_mc_main_statistic = models.CharField(max_length=120, blank=True, null=True, default='')
    opp_print = models.ImageField(upload_to='matches_results/', default=None, blank=True, null=True)
    match_winner = models.CharField(max_length=24, blank=True, null=True, default='', choices=RESULTS_CHOICE)
    match_mc_main_statistic = models.CharField(max_length=120, blank=True, null=True, default='')
    match_opp_main_statistic = models.CharField(max_length=120, blank=True, null=True, default='')
    match_creator = models.ManyToManyField(User, related_name='match_creator', blank=False)
    opponent = models.ManyToManyField(User, related_name='opponent', blank=False, default=None)
