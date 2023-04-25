
import datastore_util

def api_key_setup_card():
    """Returns card prompting user to click button ton configure bot."""

    text_widget = { 
        "decoratedText": {
            "text": "You must configure this bot before you can use it.",
            "wrapText": True
        }
    }

    button_widget = {
        "buttonList": {
            "buttons": [
                {
                    "text": "Settings",
                    "onClick": {
                        "action": {
                          "function": "get_api_key_dialog",
                          "interaction" : "OPEN_DIALOG"
                        }
                    },
                    "altText": ""
                }
            ]
        }
    }

    section = {"widgets": [text_widget, button_widget]}

    header = {"title": "Configure ChatGPT Bot"}

    cards = {
        "cardsV2": [
            {
                "cardId": "setup-card",
                "card": {
                    "name": "Setup Card",
                    "header": header,
                    "sections": [section]
                },
            }
        ]
    }

    return cards


def handle_save_api_key(event_data):
    """Handles incoming dialog event to save API key."""

    user_name = event_data['user']['name']
    user_id = user_name.split("/")[1]
    form_inputs = event_data['common']['formInputs']
    api_key = form_inputs['api_key']['stringInputs']['value'][0]

    datastore_util.store_api_key(user_id, api_key)
    return {
            'actionResponse': {
                'type': 'DIALOG',
                'dialogAction': {
                    'dialog': {
                        'body': {
                            "sections": [
                                {
                                    "widgets": [
                                        {
                                            "decoratedText": {
                                                "topLabel": "",
                                                "text": "API key saved.",
                                                "bottomLabel": "",
                                                "wrapText": True
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
            }
        }

def api_key_dialog():
    """Returns a dialog for user to enter OpenAI API key."""

    return {
        'action_response': {
            'type': 'DIALOG',
            'dialog_action': {
                'dialog': {
                    'body': {
                        "sections": [
                            {
                                "widgets": [
                                    {
                                        "decoratedText": {
                                            "topLabel": "",
                                            "text": "Enter your OpenAI API Key to use this bot. "\
                                                    "You can find it in your account settings."\
                                                    "<br /><br />"\
                                                    "<a href=\"https://platform.openai.com/account/api-keys\">"\
                                                    "OpenAI Account Settings</a><br />",
                                            "bottomLabel": "",
                                            "wrapText": True
                                        }
                                    },
                                    {
                                        "textInput": {
                                            "label": "OpenAI API Key",
                                            "type": "SINGLE_LINE",
                                            "name": "api_key",
                                            "hintText": "sk-xxxxxxxxxxx",
                                            "value": ""
                                        }
                                    },
                                    {
                                        "decoratedText": {
                                            "topLabel": "NOTE:",
                                            "text": "Your OpenAI account will be billed "\
                                                    "based on the usage of this bot.",
                                            "bottomLabel": "",
                                            "wrapText": True
                                        }
                                    },
                                    {
                                        "buttonList": {
                                            "buttons": [
                                                {
                                                    "text": "Save",
                                                    "onClick": {
                                                        "action": {
                                                            "function": "save_api_key",
                                                            "parameters": []
                                                        }
                                                    },
                                                    "altText": ""
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }
    }
