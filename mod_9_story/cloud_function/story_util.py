import gpt_util
import datastore_util
import logging

def handle_story_command(user_text, thread_id):
    """Handles user prompt for a new story."""

    title_widget = create_story_title(user_text)

    story_prompt = "Write the first section of a story in the style of a "\
        "'choose your own adventure book'. Each section should be 3 "\
        "paragraphs, and then offer 3 choices for the reader to continue. "\
        "The story should be based on the following suggestion: %s" % user_text

    messages = [{"role": "user", "content": story_prompt}]
    chapter_widgets, messages = create_story_chapter(messages)

    datastore_util.store_messages(thread_id, messages, "story")

    all_widgets = [title_widget]
    all_widgets.extend(chapter_widgets)

    cards = {
        "cardsV2": [
            {
                "cardId": "story-card",
                "card": { "sections": [ { "widgets": all_widgets } ] },
            }
        ]
    }

    return cards

def create_story_title(user_text):
    """Uses ChatGPT to create title of story based on topic provided."""

    prompt = "The following text was given as the topic of a story. Please "\
        "come up with a witty title for the story. It should be no longer "\
        "than 8 words: %s" % user_text

    story_title = gpt_util.get_gpt_response([{"role": "user", "content": prompt}])

    title_widget = {
        "decoratedText": {
            "text": f"<b>{story_title}</b>",
            "wrapText": True
        }
    }
    
    return title_widget


def create_story_chapter(messages):
    """Creates a card for a story chapter.
    
    Gets new chapter text using provided messages. Generates an image
    related to the new chapter text.
    """

    chapter_text = gpt_util.get_gpt_response(messages)
    chapter_widget = {
        "textParagraph": {
            "text": chapter_text
        }
    }

    # add new response to message history
    messages.append( {"role": "assistant", "content": chapter_text} )

    # make a copy of the messages
    image_messages = messages[:]
    prompt = "Write a prompt with a maximum of 30 words to create an "\
            "illustrated image for this most recent part of the story:\r\n %s" % chapter_text
    
    image_messages.append({"role": "user", "content": prompt})
    image_prompt = gpt_util.get_gpt_response(image_messages)
    image_prompt = f"{image_prompt}. This should be an illustration "\
                    "for a children's book in the style of an acrylic painting."
    logging.info("Story chapter image prompt: %s" % image_prompt )

    image_url = gpt_util.create_image_with_prompt(image_prompt)
    image_widget = {
        "image": {
            "imageUrl": image_url
        }
    }

    widgets = [image_widget, chapter_widget]

    # add The End to bottom if last message of story
    if len(messages) == 10:
        end_widget = {
          "decoratedText": {
            "text": "<b>The End</b>",
            "startIcon": {
              "knownIcon": "BOOKMARK"
            }
          }
        }
        widgets.append(end_widget)

    return widgets, messages


def process_story_message(thread_id, user_text, messages):
    """Processes a response from user for the next path of the story."""

    # wrap up the story after 4 choices
    if len(messages) == 8:
        user_text = "End the story with this option: %s" % user_text

    messages.append({"role": "user", "content": user_text})
    chapter_widgets, messages = create_story_chapter(messages)

    datastore_util.store_messages(thread_id, messages, "story")

    cards = {
        "cardsV2": [
            {
                "cardId": "story-card",
                "card": { "sections": [ { "widgets": chapter_widgets } ] },
            }
        ]
    }

    return cards
