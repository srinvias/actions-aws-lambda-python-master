import json
import pyjokes
import pandas


def sample(event, context):
    body = {
        "message": "Greetings from Githun. Your function is deployed by a Github Actions. Enjoy your joke",
        "joke":pyjokes.get_joke()
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

