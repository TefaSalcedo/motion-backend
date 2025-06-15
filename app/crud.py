from app.models import MotionDataModel  # importa tu modelo de datos
from pymongo.collection import Collection
from typing import List, Optional
from bson import ObjectId

# CREATE
def create_motion(collection: Collection, data: MotionDataModel) -> dict:
    # Insertamos el nuevo documento a la colección
    result = collection.insert_one(data.dict(by_alias=True))
    return {"inserted_id": str(result.inserted_id)}

# READ - Obtener todos
def get_all_motions(collection: Collection) -> List[MotionDataModel]:
    motions = []
    for doc in collection.find():
        doc["_id"] = str(doc["_id"])  # Convertir ObjectId a string
        motions.append(MotionDataModel(**doc))
    return motions

# READ - Obtener uno por ID
def get_motion_by_id(collection: Collection, id: str) -> Optional[MotionDataModel]:
    doc = collection.find_one({"_id": ObjectId(id)})
    if doc:
        doc["_id"] = str(doc["_id"])
        return MotionDataModel(**doc)
    return None

# UPDATE
def update_motion(collection: Collection, id: str, data: dict) -> bool:
    result = collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return result.modified_count > 0

# DELETE
def delete_motion(collection: Collection, id: str) -> bool:
    result = collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
