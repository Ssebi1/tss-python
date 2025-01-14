def ok_response(message, data=None):
    return {
        'status': 'success',
        'message': message,
        'data': data,
    }