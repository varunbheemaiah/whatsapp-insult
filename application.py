from flask import Flask, request
from flask_cors import CORS
import requests
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)
CORS(app)

insultFile = open('static/insults.txt')
insults = list(insultFile)
insultFile.close()

@app.route('/', methods = ['POST'])
def sendInsult():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if '!insult' in incoming_msg:
        msg.body(random.choice(insults).strip())
        responded = True
    if not responded:
        msg.body("I'm sorry, what language are you speaking? It sounds like bullshit because that's an invalid command")
    return str(resp)

if __name__ == "__main__":
    app.run()