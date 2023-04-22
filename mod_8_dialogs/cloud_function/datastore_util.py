import logging

from google.cloud import ndb
from models import *

datastore_client = ndb.Client()

def store_messages(thread_id, messages=[], thread_type=""):
    """Stores a list of messages for the thread_id.

    Uses get_or_insert() to ensure only one Thread entity exists per thread_id.
    """

    if not thread_id:
        return

    with datastore_client.context():
        thread = Thread.get_or_insert(thread_id)
        thread.message_history = { "messages" : messages }
        thread.thread_type = thread_type
        thread.put()

def get_thread(thread_id):
    """Returns thread_obj for thread_id."""

    if not thread_id:
        return None

    with datastore_client.context():
        thread_obj = Thread.get_by_id(thread_id)
        return thread_obj

def store_api_key(user_id, api_key):
    """Stores an API key for a user.

    Uses get_or_insert() to ensure only one User entity exists per user_id.
    """

    with datastore_client.context():
        user = User.get_or_insert(user_id)
        user.api_key = api_key
        user.put()

def get_api_key(user_id):
    """Returns API key for user_id."""

    with datastore_client.context():
        user = User.get_by_id(user_id)
        if user:
            return user.api_key
        else:
            return None