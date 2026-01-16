from django.views.decorators.http import require_GET

from .models import Game
from .serializers import GameSerializer


@require_GET
def game_list(request):
    category = request.GET.get('category')
    platform = request.GET.get('platform')
    games = Game.objects.filter(category__name=category).filter(platform__name=platform)

    serializer = GameSerializer(games, request=request)
    return serializer.json_response()
