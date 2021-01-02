from pymongo import MongoClient


dbUrl = "mongodb://localhost:27017"


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(dbUrl)
