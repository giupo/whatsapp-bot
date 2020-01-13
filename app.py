#!/usr/bin/env python3

import requests

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/bot', methods=['POST', 'GET'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = '%s (%s)' % (data["content"], data["author"])
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        msg.media("https://cataas.com/cat")
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')

    return str(resp)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
