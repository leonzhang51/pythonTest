from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import (
    BaseModel,
)  # pydantic is a library for defining data models in Python, which allow you to validate and parse data.
from pymongo import MongoClient
from src.route.route import router

# from src.db.dbConnection import connect_to_mongo


# # items=["foo","bar","baz","qux", "quux", "corge", "grault", "garply", "waldo", "fred", "plugh", "xyzzy","thud"]
app = FastAPI()


# class Item(BaseModel):
#     text: str = None
#     is_done: bool = False


# items = []


# @app.get("/")
# def root():
#     connect_to_mongo()
#     return {"message": "Hello World"}


# @app.post("/items")
# def create_item(item: Item):
#     items.append(item)
#     return items


# @app.get(
#     "/items/{item_id}", response_model=Item
# )  # response_model=Item means that the response will be a Item object
# def get_item(item_id: int) -> Item:
#     if item_id >= len(items):
#         raise HTTPException(status_code=404, detail=f"Item not found")
#     return items[item_id]


# @app.get("/items", response_model=list[Item])
# def read_items(limit: int = 10):
#     return items[0:limit]


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     if item_id >= len(items):
#         raise HTTPException(status_code=404, detail=f"Item not found")
#     items[item_id] = item
#     return items[item_id]


@app.on_event("startup")
async def startup_db_client():
    print("start application")


@app.on_event("shutdown")
async def shutdown_db_client():
    print("shutdown application")


app.include_router(router)
