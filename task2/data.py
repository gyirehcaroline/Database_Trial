from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://mongo:agKvmIMvyJiUFElCTdjQMUZqLVjzkklB@junction.proxy.rlwy.net:27999")
db = client["shipping_dataset"]

# Collections
customers_collection = db["Customers"]
products_collection = db["Products"]
orders_collection = db["Orders"]
shipments_collection = db["Shipments"]
