from pymongo import MongoClient
from bson import json_util, ObjectId
import json
from .models import PersonModel, UpdatePersonModel, CreatePersonModel

uri = "mongodb://localhost:27017/"
db_name = "mydatabase"


class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)  # this will return the ID as a string
        return json.JSONEncoder.default(self, o)


def connect_to_mongodb(uri, db_name) -> MongoClient:
    try:
        client = MongoClient(uri)
        db = client[db_name]
        print(f"Connected to MongoDB database: {db_name}")
        return db
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
# if __name__ == "__main__":
#     uri = "mongodb://localhost:27017/"
#     db_name = "mydatabase"
#     db = connect_to_mongodb(uri, db_name)


def get_people_by_name(name: str):

    try:
        db: MongoClient = connect_to_mongodb(uri, db_name)
        return_list = []
        result = db.customers.find({"name": name})
        for x in result:
            x["_id"] = str(x["_id"])
            return_list.append(x)
        return list(return_list)
        # return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_people_by_address(address: str):
    try:
        db: MongoClient = connect_to_mongodb(uri, db_name)
        return_list = []
        result = db.customers.find({"address": address})
        for x in result:
            x["_id"] = str(x["_id"])
            return_list.append(x)
        return list(return_list)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_all_people():
    return_list = []
    try:
        db: MongoClient = connect_to_mongodb(uri, db_name)
        result = db.customers.find()
        for x in result:
            x["_id"] = str(x["_id"])
            return_list.append(x)
        return list(return_list)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def update_person(person_id: str, name: str, address: str):
    try:
        db: MongoClient = connect_to_mongodb(uri, db_name)
        result = db.customers.update_one(
            {"_id": ObjectId(person_id)}, {"$set": {"name": name, "address": address}}
        )
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def delete_person(person_id: str):
    try:
        db: MongoClient = connect_to_mongodb(uri, db_name)
        result = db.customers.delete_one({"_id": ObjectId(person_id)})

        return result.deleted_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def delete_all_people():
    try:
        db: MongoClient = connect_to_mongodb(uri, db_name)
        result = db.customers.delete_many({})
        return result.deleted_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def create_person(name: str, address: str):
    try:
        db: MongoClient = connect_to_mongodb(uri, db_name)
        return_list = []
        result = db.customers.insert_one({"name": name, "address": address})
        for x in result:
            x["_id"] = str(x["_id"])
            return_list.append(x)
        return list(return_list)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def create_peopples(people: list):
    try:
        db: MongoClient = connect_to_mongodb(uri, db_name)
        result = db.customers.insert_many(people)
        return result.inserted_ids
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
