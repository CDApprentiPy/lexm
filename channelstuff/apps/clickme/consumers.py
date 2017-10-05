from channels import Group
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels.sessions import channel_session
import json

# def http_consumer(message):
#     # Make standard HTTP response - access ASGI path attribute directly
#     response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
#     # Encode that response into message format (ASGI)
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)

# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     message.reply_channel.send({
#         "text": message.content['text'],
#     })

@channel_session
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("counter").add(message.reply_channel)
    try:
        message.channel_session['count'] = message.channel_session['count'] + 1
    except:
        message.channel_session['count'] = 0
    message.reply_channel.send({
        'text': json.dumps({
            'count': message.channel_session['count'],
        })
    })

@channel_session
def ws_increment(message):
    count = message.channel_session['count'] + 1
    message.channel_session['count'] = count
    Group("counter").send({
        "text": json.dumps({
            "count": message.channel_session['count']
        })
    })
