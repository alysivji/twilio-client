from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# TODO use fuzzywuzzy for matching

app = Flask(__name__)


@app.route('/twilio', methods=['POST'])
def reply_to_message():
    """Send a reply based on incoming message"""

    # import pdb; pdb.set_trace()
    body = request.values.get('Body', None)

    # Twilio Reponse
    resp = MessagingResponse()

    if body == 'hi':
        resp.message('hi right back')
    elif body == 'trello':
        resp.message('Adding task to board')
    else:
        resp.message('Unknown. Try again')

    return str(resp)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )
