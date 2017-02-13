import json


def print_json(result):
    print(json.dumps(result, indent=4))

def result_json(code, message):
    return {
        'code': code,
        'message': message if code == 204 else 'Error!'
    }
