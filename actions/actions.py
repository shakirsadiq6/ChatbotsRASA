# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib
import smtplib
import os
from dotenv import load_dotenv

class ActionWelcomeMessage(Action):

    def name(self) -> Text:
        return "action_welcome_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Hi Chappie here😎, your virtual assistant.👋"
        response2 = "What brought you here today?"
        welcomebuttons = ['Using chatbot 👉', 'I have questions 🙂', 'Just browsing 🙄']

        buttons = []
        for i in welcomebuttons:
            buttons.append({"title": i, "payload": i})
        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons=buttons)
        return []


class ActionQuestions(Action):

    def name(self) -> Text:
        return "action_ihavequestions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "I'll be more than happy to answer all your questions!"
        response2 = "What information are you looking for?"
        questionbuttons = ['🤝Contact sales', '🚀 Features', '⚙ Integrations', '📧 Contact us']

        buttons = []
        for i in questionbuttons:
            buttons.append({"title": i, "payload": i})
        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons=buttons)
        return []

class ActionJustBrowsing(Action):

    def name(self) -> Text:
        return "action_justbrowsing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Got it! If you have any other questions, feel free to start the chat again. 🙌"
        response2 = "Have fun browsing our website! 👋"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        return []

class ActionContactSales(Action):

    def name(self) -> Text:
        return "action_contactsales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Before we start, please answer the following questions."
        response2 = "Do you agree to have your personal data processed?"
        response3 = "ℹ To see our Privacy Policy, select the button below."

        salesbuttons = ['👍 I agree', '👎 I do not agree', '📃 Privacy policy']

        buttons = []
        for i in salesbuttons:
            buttons.append({"title": i, "payload": i})

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        dispatcher.utter_message(text= response3, buttons=buttons)
        return []

class ActionIAgree(Action):

    def name(self) -> Text:
        return "action_iagree"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Great! 💪"
        response2 = "I just need more information to find the right person for you. 😊"
        response3 = "what's your business email address?"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        dispatcher.utter_message(text= response3)
        return []

class ActionDontAgree(Action):

    def name(self) -> Text:
        return "action_idontagree"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dontagreebuttons = ['👈 Go to main menu', '🤔 I have changed my mind']

        buttons = []
        for i in dontagreebuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "Got it!"
        response2 = "What would you like to do next?"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons= buttons)
        return []

class ActionIntegrations(Action):

    def name(self) -> Text:
        return "action_integrations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        integrationbuttons = ['🤝Contact sales', '👈 Go to main menu']

        buttons = []
        for i in integrationbuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "We offers integrations with websites, mobile apps, and also with other popular apps like FB, LI, TW and more."
        response2 = "Want to know more?"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons= buttons)
        return []

class ActionIntegrations(Action):

    def name(self) -> Text:
        return "action_contactus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "I'll ask you a couple of questions and pass your message to our team. Let's begin! 👉"
        response2 = "what's your business email address?"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        return []

class ActionEmail(Action):

    def name(self) -> Text:
        return "action_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        emailbuttons = ['🤝Contact sales', '👈 Go to main menu']

        buttons = []
        for i in emailbuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "Thank you! 👍 We'll get back to you soon 😊"
        response2 = "What would you like to do next?"

        # All the previous messages
        user_input = []
        for event in tracker.events:
            if event.get("event") == "user":
                user_input.append(event.get("text"))

        load_dotenv()

        to_email = os.getenv("to_email")
        sender_email = os.getenv("sender_email")
        sender_password = os.getenv("sender_password")
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(sender_email, sender_password)
        header = 'To:' + to_email + '\n' + 'From: ' + sender_email + '\n' + 'Subject:Message From Drish Chatbot \n'
        message = header + f'\n {user_input[-1]}\n\n'
        smtpserver.sendmail(sender_email, to_email, message)
        print('done!')
        smtpserver.quit()

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons= buttons)
        return []

class ActionFeatures(Action):

    def name(self) -> Text:
        return "action_features"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        featuresbuttons = ['Conversational UI', 'Grows Revenue', 'Improve customer acquisition']

        buttons = []
        for i in featuresbuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "ChatBot provides a wide range of features that let you automate your customer communication with ease."
        response2 = "Which one would you like to know more about?"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons= buttons)
        return []

class ActionConversationalUI(Action):

    def name(self) -> Text:
        return "action_conversationalui"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cuibuttons = ['🤝Contact sales', '👈 Go to main menu']

        buttons = []
        for i in cuibuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "A powerful conversational interface pushes the brand for deeper levels of engagement with their customers."

        dispatcher.utter_message(text= response1, buttons= buttons)
        return []

class ActionGrowthRevenue(Action):

    def name(self) -> Text:
        return "action_growthrevenue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        grbuttons = ['🤝Contact sales', '👈 Go to main menu']

        buttons = []
        for i in grbuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "With smart and reliable responses, customers will feel happy and satisfied with services, which means higher conversation rates."

        dispatcher.utter_message(text= response1, buttons= buttons)
        return []

class ActionCustomerAcquisition(Action):

    def name(self) -> Text:
        return "action_customeracquisition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cabuttons = ['🤝Contact sales', '👈 Go to main menu']

        buttons = []
        for i in cabuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "Faster response time, 24/7 customer support & high degree of accuracy resulting in high-quality support."

        dispatcher.utter_message(text= response1, buttons= buttons)
        return []

class ActionPrivacyPolicy(Action):

    def name(self) -> Text:
        return "action_privacypolicy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Click the below link to check our privacy policy"
        response2 = "https://www.drishinfo.com/privacy-policy/"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        return []

class ActionInitialPayload(Action):

    def name(self) -> Text:
        return "action_initialpayload"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "To initiate the conversation say “Hi”"

        dispatcher.utter_message(text= response1)
        return []