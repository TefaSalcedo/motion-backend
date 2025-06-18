# ...existing code...
from app.models import MotionDataModel, MotionCreateModel
from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Optional
from bson import ObjectId

# CREATE
async def create_motion(collection: AsyncIOMotorCollection, data: MotionCreateModel) -> dict:
    result = await collection.insert_one(data.dict(by_alias=True))
    return {"inserted_id": str(result.inserted_id)}

# READ - Obtener todos
async def get_all_motions(collection: AsyncIOMotorCollection) -> List[MotionDataModel]:
    motions = []
    async for doc in collection.find():
        doc["_id"] = str(doc["_id"])
        motions.append(MotionDataModel(**doc))
    return motions

# READ - Obtener uno por ID
async def get_motion_by_id(collection: AsyncIOMotorCollection, id: str) -> Optional[MotionDataModel]:
    doc = await collection.find_one({"_id": ObjectId(id)})
    if doc:
        doc["_id"] = str(doc["_id"])
        return MotionDataModel(**doc)
    return None

# UPDATE
async def update_motion(collection: AsyncIOMotorCollection, id: str, data: dict) -> bool:
    result = await collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return result.modified_count > 0

# DELETE
async def delete_motion(collection: AsyncIOMotorCollection, id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
