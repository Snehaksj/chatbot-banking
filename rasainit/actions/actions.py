# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import EventType
from excel_data_store import DataStore
# class ActionSaveData(Action):

#     def name(self) -> Text:
#         return "action_save_data"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         DataStore(tracker.get_slot("name"),
#                 tracker.get_slot("number"),
#                 tracker.get_slot("feedback"))
#         dispatcher.utter_message(text="Thanks for the feedback!")
#         return []

# class FormDataCollect(FormValidationAction):
#     def name(self) -> Text:
#         return "Form_Info"
    
#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["name","number","feedback"]
    
#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         return {
#            "name":[self.from_entity(entity="name")],
#            "number":[self.from_entity(entity="number")],
#            "feedback":[self.from_entity(entity="feedback")]
#         }
#     def submit(
#         self,
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:
#         return []
    
