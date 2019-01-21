## rasa-starter pack
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class ActionSetGoal(Action):
    def name(self):
        return "action_set_goal"

    def run(self, dispatcher, tracker, domain):
        usr_msg = tracker.latest_message['text']
        goal = tracker.get_slot('goal')
        print("usr_msg: {} \n goal_slot: {}".format(usr_msg, goal))
        if goal == None:
            SlotSet('goal', usr_msg)
            dispatcher.utter_template("utter_set_goal_02", tracker)
            return [SlotSet('goal', goal)]
        else:
            SlotSet('goal', goal) # Need to keep this in here to make sure template utters most recent goal
            dispatcher.utter_template("utter_set_goal_02", tracker)
            return [SlotSet('goal', goal)]
