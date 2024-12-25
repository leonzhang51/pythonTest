from typing import Optional  # Union[..., None]
import uuid
from pydantic import BaseModel, Field


class PersonModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    address: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "6763bbc527d3713ee02e5475",
                "name": "Ben",
                "address": "Apple st 652",
            }
        }


class UpdatePersonModel(BaseModel):
    name: Optional[str]
    address: Optional[str]
    _id: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "_id": "6763bbc527d3713ee02e5475",
                "name": "My important task",
                "address": "Apple st 652",
            }
        }


class CreatePersonModel(BaseModel):
    name: str = Field(...)
    address: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Ben",
                "address": "Apple st 652",
            }
        }
