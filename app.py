# Ref: https://github.com/bhavaniravi/rasa-site-bot
from flask import Flask
from flask import render_template, jsonify, request
import requests
import json
# from models import *
from engine import *
import random

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import AvailableEndpoints

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

get_random_response = lambda intent:random.choice(intent_response_dict[intent])

# Load Rasa NLU interpreter and Rasa Core agent
interpreter = RasaNLUInterpreter("models/livio/nlu")
_endpoints = AvailableEndpoints.read_endpoints("endpoints.yml")
action_endpoint = _endpoints.action
agent = Agent.load("models/livio/dialouge", interpreter=interpreter, action_endpoint=action_endpoint)

@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        response = requests.get("http://localhost:5000/parse",params={"q":user_message})
        response = response.json()
        entities = response.get("entities")
        topresponse = response["intent"]
        intent = topresponse.get("name")
        print("Intent: {}, Entities: {}".format(intent,entities))
        if intent == "fact":
            response_text = get_fact_response()
        else:
            bot_responses = agent.handle_text(response)
            bot_responses_text = [message['text'] for message in bot_responses]
            result = json.dumps(bot_responses_text)
        return jsonify({"status": "success", "responses": result})
    except Exception as e:
        print(e)
        return jsonify({"status": "success", "response": "Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
