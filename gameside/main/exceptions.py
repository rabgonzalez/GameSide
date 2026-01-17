from rest_framework.views import exception_handler


def exceptionHandler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        json_response = {
            'status': 'error',
            'code': response.status_code,
            'message': response.data.get('detail', 'Error no especificado'),
        }

        if response.status_code == 405:
            json_response['message'] = 'Method not allowed'
            json_response['allowed_methods'] = response.get('Allow', 'No especificado')

        response.data = json_response

    return response
