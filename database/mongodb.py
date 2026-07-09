from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["kubewatch"]

metrics_collection = db["metrics_history"]