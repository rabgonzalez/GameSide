from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import Game
from .serializers import GameSerializer


@require_GET
def game_list(request):
    category = request.GET.get('category')
    platform = request.GET.get('platform')

    games = Game.objects.all()

    if category == None and platform != None:
        games = Game.objects.filter(platforms__name=platform)

    elif category != None and platform == None:
        games = Game.objects.filter(category__name=category)

    elif category != None and platform != None:
        games = Game.objects.filter(category__name=category, platforms__name=platform)

    serializer = GameSerializer(games, request=request)
    return serializer.json_response()


@require_GET
def game_detail(request, game_slug: str):
    game = Game.objects.filter(slug=game_slug)
    if not game.exists():
        return JsonResponse({'error': 'Game not found'}, status=404)

    serializer = GameSerializer(game, request=request)
    return serializer.json_response()
