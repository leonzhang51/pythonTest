from pymongo import MongoClient


def connect_to_mongo():
    uri = "mongodb://localhost:27017/"
    # Create a new client and connect to the server
    client = MongoClient(uri)
    try:
        dblist = client.list_database_names()
        print(dblist)
        if "mydatabase" in dblist:
            print("The database exists.")
            mydb = client["mydatabase"]
            mycol = mydb["customers"]
            for x in mycol.find():
                print("data in existed collection", x)
        else:
            mydb = client["mydatabase"]
            mycol = mydb["customers"]
            print("Database created")
            mylist = [
                {"name": "Amy", "address": "Apple st 652"},
                {"name": "Hannah", "address": "Mountain 21"},
                {"name": "Michael", "address": "Valley 345"},
                {"name": "Sandy", "address": "Ocean blvd 2"},
                {"name": "Betty", "address": "Green Grass 1"},
                {"name": "Richard", "address": "Sky st 331"},
                {"name": "Susan", "address": "One way 98"},
                {"name": "Vicky", "address": "Yellow Garden 2"},
                {"name": "Ben", "address": "Park Lane 38"},
                {"name": "William", "address": "Central st 954"},
                {"name": "Chuck", "address": "Main Road 989"},
                {"name": "Viola", "address": "Sideway 1633"},
            ]

            x = mycol.insert_many(mylist)
            # print list of the _id values of the inserted documents:
            print(x)
        client.close()
    except KeyError as e:
        print(f"Error accessing database: {e}")
