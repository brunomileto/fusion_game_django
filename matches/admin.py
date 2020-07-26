from django.contrib import admin
from matches.models import Platform, GameRule, GameMode, Game, Match, GameCategory, GameSubCategory, GameSerie

# Register your models here.

admin.site.register(GameCategory)
admin.site.register(GameSubCategory)
admin.site.register(GameSerie)
admin.site.register(Platform)
admin.site.register(GameMode)
admin.site.register(Game)
admin.site.register(Match)
admin.site.register(GameRule)
