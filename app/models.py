from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, info):  # <-- agrega el argumento info
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema, handler):
        return {'type': 'string'}
    

class MotionCreateModel(BaseModel):
    marca: str
    sucursal: str
    aspirante: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class MotionDataModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    marca: str
    sucursal: str
    aspirante: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class MotionUpdateModel(BaseModel):
    marca: Optional[str] = None
    sucursal: Optional[str] = None
    aspirante: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}