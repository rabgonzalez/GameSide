import json
import uuid

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from users.models import Token

from .models import Game, Review
from .serializers import GameSerializer, ReviewSerializer


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
    game = Game.objects.filter(slug=game_slug).first()
    if not game:
        return JsonResponse({'error': 'Game not found'}, status=404)

    serializer = GameSerializer(game, request=request)
    return serializer.json_response()


@require_GET
def review_list(request, game_slug: str):
    game = Game.objects.filter(slug=game_slug).first()
    if not game:
        return JsonResponse({'error': 'Game not found'}, status=404)

    reviews = game.reviews.all()

    serializer = ReviewSerializer(reviews, request=request)
    return serializer.json_response()


@require_GET
def review_detail(request, game_slug: str, review_id: int):
    game = Game.objects.filter(slug=game_slug).first()
    if not game:
        return JsonResponse({'error': 'Game not found'}, status=404)

    review = game.reviews.filter(id=review_id).first()
    if not review:
        return JsonResponse({'error': 'Review not found'}, status=404)

    serializer = ReviewSerializer(review, request=request)
    return serializer.json_response()


@csrf_exempt
@require_POST
def add_review(request, game_slug: str):
    try:
        payload = json.loads(request.body)

        # Esto es para forzar el KeyError en caso de que no se haya pasado alguno de los campos
        payload['rating']
        payload['comment']
        payload['game']
        payload['author']

        # Para forzar el ValueError y así hacer el Invalid authentication token
        uuid.UUID(str(request.headers['token']))

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON body'}, status=400)

    except KeyError:
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    except ValueError:
        return JsonResponse({'error': 'Invalid authentication token'}, status=400)

    if not Token.objects.filter(key=request.headers['token']).first():
        return JsonResponse({'error': 'Unregistered authentication token'}, status=401)

    if payload['rating'] < 1 or payload['rating'] > 5:
        return JsonResponse({'error': 'Rating is out of range'}, status=400)

    game = Game.objects.filter(slug=game_slug).first()

    if not game or not payload['game']['id'] == game.pk:
        return JsonResponse({'error': 'Game not found'}, status=404)

    author = get_user_model().objects.filter(id=payload['author']['id']).first()

    review = Review.objects.create(
        rating=payload['rating'],
        comment=payload['comment'],
        game=game,
        author=author,
    )

    return JsonResponse({'id': review.id})
