from pymongo import MongoClient
from app.config.settings import Config


class MongoDB:

    client = None
    db = None

    @classmethod
    def connect(cls):

        if cls.client is None:

            cls.client = MongoClient(Config.MONGO_URI)

            cls.db = cls.client[Config.DATABASE_NAME]

        return cls.db

    @classmethod
    def metrics_collection(cls):

        return cls.connect()["metrics_history"]