import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    HOST = os.getenv("HOST", "0.0.0.0")

    PORT = int(os.getenv("PORT", 5000))

    MONGO_URI = os.getenv("MONGO_URI")

    DATABASE_NAME = os.getenv("DATABASE_NAME")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")