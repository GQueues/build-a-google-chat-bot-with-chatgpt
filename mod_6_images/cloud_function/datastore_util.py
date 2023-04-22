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
