import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtenemos las variables de entorno
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "testdb")

# Creamos el cliente de MongoDB
client = AsyncIOMotorClient(MONGO_URL)

# Seleccionamos la base de datos
database = client[DATABASE_NAME]

# Esta función la podemos usar para traer la db donde la necesitemos
def get_database():
    return database