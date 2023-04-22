from google.cloud import ndb

class Thread(ndb.Model):
    message_history = ndb.JsonProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

    def get_messages(self):
        return self.message_history['messages']
