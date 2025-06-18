import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient


load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "testdb")


client = AsyncIOMotorClient(MONGO_URL)


database = client[DATABASE_NAME]

def get_database():
    return database