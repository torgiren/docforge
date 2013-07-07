import pymongo
import uuid

class DummyMongo():
    def __init__(self):
        self.__dbname = str(uuid.uuid4())

    def create(self):
        self.conn = pymongo.Connection('localhost')
        self.db = self.conn[self.__dbname]
        return self.db

    def delete(self):
        self.conn.drop_database(self.__dbname)

