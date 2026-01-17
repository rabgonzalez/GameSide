from django.http import JsonResponse


def custom_405(request, exception):
    return JsonResponse({'Error', 'Method not allowed'}, status=405)
