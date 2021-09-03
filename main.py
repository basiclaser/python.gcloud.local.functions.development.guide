# [START functions_http_template]
# [START functions_pubsub_template]
from flask import escape, abort
# [END functions_pubsub_template]
# [END functions_http_template]


# [START functions_http_template]
def http_template(request):
    """
        HTTP-triggered functions receive a "request" object that contains info about the HTTP request.
        HTTP requests 99% of the time expect a response, otherwise the request will eventually "timeout".

        This cloud function looks for JSON or text in the request, and returns a response.
        If the request body is not JSON or text, it returns a "400 Bad Request" error.
    """
    import json
    try:

        content_type = request.headers['content-type']
        if content_type == 'application/json':
            request_json = request.get_json(silent=True)
            print(json.dumps(request_json, indent=2))
        elif content_type == 'text/plain':
            print(request.data)
        return 'I received your {} request'.format(escape(content_type)), 200

    except Exception as e:
        return 'Bad Request - you didnt POST me any JSON or text', 400
# [END functions_http_template]

# [START functions_pubsub_template]


def pubsub_template(event, context):
    """
        pubsub-triggered functions receive a "context" object that contains info about the pubsub event.
        they don't have to return anything as they are not a "request" for something like a HTTP request.
    """
    print("""This Function was triggered by messageId {} published at {} to {}
    """.format(context.event_id, context.timestamp, context.resource["name"]))
# [END functions_pubsub_template]
