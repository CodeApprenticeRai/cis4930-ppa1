'''
    This double object can be used as a stub and also mock:

    It can be used as a predefined datastore to answer calls.
    It can be used to register calls.

'''
class DatabaseDouble:
    def __init__(self):
        self.database = {}

    def store(self, key, data):
        self.database[key] = data

    def retrieve(self, key):
        return self.database.get(key, None)
