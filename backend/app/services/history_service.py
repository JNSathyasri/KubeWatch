from app.database.mongodb import MongoDB

metrics_collection = MongoDB.connect()["metrics_history"]


class HistoryService:

    @staticmethod
    def latest(limit=100):

        history = list(
            metrics_collection.find(
                {},
                {"_id": 0}
            )
            .sort("timestamp", -1)
            .limit(limit)
        )

        history.reverse()

        return history