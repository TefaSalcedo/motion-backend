from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_database  # usa la función para obtener la db
from app.models import MotionDataModel
from app.models import MotionCreateModel
from app.models import MotionUpdateModel
from app import crud
from bson import ObjectId

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API funcionando 🏁"}

@app.get("/ping-mongo")
async def ping_mongo():
    db = get_database()
    collections = await db.list_collection_names()
    return {"collections": collections}

# GET ALL
@app.get("/motions", response_model=list[MotionDataModel])
async def get_all_motions():
    motions = await crud.get_all_motions(get_database()["motions"])
    return motions

# GET BY ID
@app.get("/motions/{id}", response_model=MotionDataModel)
async def get_motion(id: str):
    motion = await crud.get_motion_by_id(get_database()["motions"], id)
    if motion is None:
        raise HTTPException(status_code=404, detail="Motion not found")
    return motion


# CREATE
@app.post("/motions", response_model=dict)
async def create_motion(data: MotionCreateModel):
    result = await crud.create_motion(get_database()["motions"], data)
    return result

# UPDATE
@app.put("/motions/{id}", response_model=dict)
async def update_motion(id: str, data: MotionUpdateModel):
    updated = await crud.update_motion(
        get_database()["motions"], 
        id, 
        data.dict(exclude_unset=True))
    
    motion = await get_database()["motions"].find_one({"_id": ObjectId(id)})
    
    if not motion:
        raise HTTPException(status_code=404, detail="Motion not found")
    
    motion["_id"] = str(motion["_id"])
    return motion



# DELETE
@app.delete("/motions/{id}", response_model=dict)
async def delete_motion(id: str):
    deleted = await crud.delete_motion(get_database()["motions"], id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Motion not found")
    return {"message": "Motion deleted"}