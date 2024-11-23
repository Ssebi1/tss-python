def ok_response(message, data=None):
    return {
        'status': 'ok',
        'message': message,
        'data': data,
    }