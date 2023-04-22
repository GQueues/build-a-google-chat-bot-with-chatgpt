import flask
import functions_framework
import logging
import google.cloud.logging
import openai
from auth_util import is_request_valid

# TODO: put in your own OpenAI API key
MY_API_KEY = "sk-xxxxxxxxxxxxxxxxxxx"

import gpt_util

logging_client = google.cloud.logging.Client()
logging_client.setup_logging(log_level=logging.INFO)

@functions_framework.http
def handle_chat(request):
    """Handles incoming messages from Google Chat."""

    # verify request is from Google before doing anything
    if not is_request_valid(request):
        return "Unauthorized request"

    event_data = request.get_json()
    logging.info("received event_data %s" % event_data)
    event_type = event_data['type']

    # Bot added
    if event_type == 'ADDED_TO_SPACE':
        
        # Added to a room
        if event_data['space']['type'] == 'ROOM':
            return { "text" : f"Thanks for adding me to the room. "\
                    "Mention me in a conversation whenever you need help." }

        # Added to a DM
        elif event_data['space']['type'] == 'DM':
            user_display_name = event_data['user']['displayName']
            return { "text" : f"Hi {user_display_name}! I'm here to help "\
                     "whenever you need it."}

    # Bot removed
    elif event_type == 'REMOVED_FROM_SPACE':
        return {}

    # A normal message event
    elif event_type == 'MESSAGE':
        return process_message_event(event_data)


def process_message_event(event_data):
    """Processes message event."""

    incoming_message = event_data.get('message', {})
    user_text = incoming_message.get('argumentText', "")
    user_name = event_data['user']['name']

    logging.info("user_text %s" % user_text)
    
    openai.api_key = MY_API_KEY

    messages = []

    # set guidance for ChatGPT
    guidance = "You are helpful assistant who has a cheerful attitude"
    messages.append({"role": "system", "content" : guidance})

    # add new message to list
    messages.append( {"role": "user", "content": user_text} )

    # get new gpt response
    try:
        gpt_response = gpt_util.get_gpt_response(messages)
    except openai.error.OpenAIError as e:
        return { "text" : str(e)}

    chat_response = { 
        "text" : gpt_response
    }

    logging.info("chat_response: %s" % chat_response)

    return chat_response


