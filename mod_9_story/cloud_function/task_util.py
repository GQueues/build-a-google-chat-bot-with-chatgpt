import logging
import json
from google.cloud import tasks_v2
import openai
import story_util
import auth_util
import datastore_util

# TODO: Update with Google Cloud ProjectID
PROJECT_ID = "XXXXXXX"

# TODO: Update with Cloud Functions Service Account
SERVICE_ACCOUNT_EMAIL = "xxxxxxxxxxxxxxx"

# TODO: Update with Cloud Functions Trigger Url
TRIGGER_URL = "xxxxxxxxxxxxx"


def run_as_background_task(action, thread_id, user_text, message_id_to_update):
    """Creates a task in Google Cloud Tasks for the specified action."""

    tasks_client = tasks_v2.CloudTasksClient()

    payload = {
        "background_task" : True,
        "action" : action,
        "thread_id" : thread_id,
        "user_text" : user_text,
        "message_id_to_update" : message_id_to_update
    }

    logging.info(f"run_as_background_task: {action}")

    # Convert dict to JSON string
    payload = json.dumps(payload)

    LOCATION = "us-central1"
    QUEUE = "story-queue"

    parent = tasks_client.queue_path(PROJECT_ID, LOCATION, QUEUE)

    converted_payload = payload.encode()

    task = {
        "http_request": {
            "http_method": tasks_v2.HttpMethod.POST,
            "url": TRIGGER_URL,
            "headers": {"Content-type": "application/json"},
            "oidc_token": {
                "service_account_email": SERVICE_ACCOUNT_EMAIL,
                "audience": TRIGGER_URL
            },
            "body" : converted_payload
        }
    }

    response = tasks_client.create_task(request={"parent": parent, "task": task})


def process_background_task(request):
    """Processes a request from Google Cloud Tasks.
    
    Verifies request before processing.
    """

    if not auth_util.is_backround_request_valid(request):
        return "Unauthorized request"

    task_data = request.get_json()
    logging.info(f"task_data: {task_data}")

    action = task_data.get("action")
    thread_id = task_data.get("thread_id")
    user_text = task_data.get("user_text")
    message_id_to_update = task_data.get("message_id_to_update")
    space_id = thread_id.split("-")[1]
    space_name = f"spaces/{space_id}"
    user_id = thread_id.split("-")[0]

    # get api_key
    try:
        api_key = datastore_util.get_api_key(user_id)
        openai.api_key = api_key
    except:
        from main import MY_API_KEY
        openai.api_key = MY_API_KEY


    if action == "process_story_message":
        story_util.process_story_message(thread_id, user_text, message_id_to_update)
    
    elif action == "handle_story_command":
        story_util.handle_story_command(thread_id, user_text, message_id_to_update)
    
    return {}

