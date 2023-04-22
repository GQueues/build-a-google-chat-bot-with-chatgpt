import flask
import functions_framework
import logging
import google.cloud.logging

logging_client = google.cloud.logging.Client()
logging_client.setup_logging(log_level=logging.INFO)

@functions_framework.http
def handle_chat(request):
    """Handles incoming messages from Google Chat."""
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

    return {"text" : f"You said: {user_text}"}

    