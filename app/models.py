from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v, info=None):  # info es opcional para compatibilidad
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    @classmethod
    def __get_pydantic_json_schema__(cls, schema, handler):
        return {'type': 'string'}

class CommonConfig:
    allow_population_by_field_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}

class CustomBaseModel(BaseModel):
    class Config(CommonConfig):
        pass

class MotionCreateModel(CustomBaseModel):
    marca: str
    sucursal: str
    aspirante: str

class MotionDataModel(CustomBaseModel):
    id: Optional[str] = Field(alias="_id")
    marca: str
    sucursal: str
    aspirante: str

class MotionUpdateModel(CustomBaseModel):
    marca: Optional[str] = None
    sucursal: Optional[str] = None
    aspirante: Optional[str] = None