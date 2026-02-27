from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform', 'status', 'hours_played']
    list_filter = ['status', 'platform']
    search_fields = ['title']
