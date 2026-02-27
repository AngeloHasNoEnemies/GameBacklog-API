from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Game
from .serializers import GameSerializer


@extend_schema_view(
    list=extend_schema(summary="List all games in the backlog"),
    create=extend_schema(summary="Add a new game to the backlog"),
    retrieve=extend_schema(summary="Retrieve a single game by ID"),
    update=extend_schema(summary="Update all fields of a game"),
    partial_update=extend_schema(summary="Partially update a game"),
    destroy=extend_schema(summary="Delete a game from the backlog"),
)
class GameViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing the game backlog.
    Supports full CRUD: list, create, retrieve, update, partial_update, destroy.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
