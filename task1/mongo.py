from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://mongo:agKvmIMvyJiUFElCTdjQMUZqLVjzkklB@junction.proxy.rlwy.net:27999")  # Adjust as needed
db = client["shipping_dataset"]

import os
print("Current working directory:", os.getcwd())

# Load the dataset
dataset = pd.read_csv("dataset.csv")
print(dataset)


# Define collections
customers_collection = db["Customers"]
products_collection = db["Products"]
orders_collection = db["Orders"]
shipments_collection = db["Shipments"]


# Define schemas for collections
customers_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["gender", "priorPurchases", "customerCareCalls", "customerRating",],
        "properties": {
            "gender": {"bsonType": "string", "enum": ["Male", "Female"], "description": "Gender must be either 'Male' or 'Female'"},
            "priorPurchases": {"bsonType": "int", "minimum": 0, "description": "Prior Purchases must be a non-negative integer"},
            "customerCareCalls": {"bsonType": "int", "minimum": 0, "description": "Customer care calls must be a non-negative integer"},
            "customerRating": {"bsonType": "int", "minimum": 1, "maximum": 5, "description": "Customer rating must be between 1 and 5"},
        }
    }
}

products_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["cost", "productImportance", "weightInGms"],
        "properties": {
            "cost": {"bsonType": "double", "minimum": 0, "description": "Cost must be a non-negative number"},
            "productImportance": {"bsonType": "string", "enum": ["low", "medium", "high"], "description": "Product Importance must be 'low', 'medium', or 'high'"},
            "weightInGms": {"bsonType": "double", "minimum": 0, "description": "Weight must be a non-negative number"}
        }
    }
}

orders_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["discountOffered"],
        "properties": {
            "discountOffered": {"bsonType": "double", "minimum": 0, "description": "Discount must be a non-negative number"},
        }
    }
}

shipments_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["warehouseBlock", "modeOfShipment"],
        "properties": {
            "warehouseBlock": {"bsonType": "string", "enum": ["A", "B", "C", "D", "E"], "description": "Warehouse block must be one of 'A', 'B', 'C', 'D', or 'E'"},
            "modeOfShipment": {"bsonType": "string", "enum": ["Ship", "Flight", "Road"], "description": "Mode of shipment must be 'Ship', 'Flight', or 'Road'"}
        }
    }
}

# Create or update collections with schema validation
def create_or_update_collection(collection_name, schema):
    if collection_name in db.list_collection_names():
        db.command({"collMod": collection_name, "validator": schema})
    else:
        db.create_collection(collection_name, validator=schema)

create_or_update_collection("Customers", customers_schema)
create_or_update_collection("Products", products_schema)
create_or_update_collection("Orders", orders_schema)
create_or_update_collection("Shipments", shipments_schema)


print("Data insertion completed successfully!")