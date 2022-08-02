from pymongo import MongoClient


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Database:
    db = None
    client = None

    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client['notes_library']

    def get_db(self):
        return self.db
