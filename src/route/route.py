from src.handler.handler import *
from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/", response_description="List all people")
async def get_people():
    people = get_all_people()
    if people:
        print("data in existed collection")
        for x in people:
            print("data in existed collection", x.get("address"))
        return people

    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content="No people available"
    )


@router.get("/{name}", response_description="Get a single person")
async def get_person(name):
    person = get_people_by_name(name)
    if person:
        return person
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content="Person not found"
    )


@router.post("/", response_description="Add new person")
async def add_person(request: Request):
    data = await request.json()
    person = create_person(data.get("name"), data.get("address"))
    print("data in existed collection", person)
    return person


@router.put("/{person_id}", response_description="Update a person")
async def update_person_data(person_id: str, request: Request):
    data = await request.json()
    person = update_person(person_id, data.get("name"), data.get("address"))
    print("data in existed collection", person.raw_result)
    if person.raw_result:
        return {
            "message": "Person with ID: {} name and address updated".format(person_id)
        }
    return {"message": "Person not found"}


@router.delete("/{person_id}", response_description="Delete a person")
async def delete_person_data(person_id: str):
    person = delete_person(person_id)
    if person:
        return {"message": "Person with ID: {} removed".format(person_id)}
    return {"message": "Person not found"}
