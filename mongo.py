from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient("mongodb://mongo:agKvmIMvyJiUFElCTdjQMUZqLVjzkklB@junction.proxy.rlwy.net:27999")  # Adjust as needed
db = client["shipping_dataset"]  # Replace with your database name

# Create collections
customers_collection = db["customers"]
shipments_collection = db["shipments"]
customer_interactions_collection = db["customerInteractions"]

# Drop collections if they already exist for fresh insertion (optional)
customers_collection.drop()
shipments_collection.drop()
customer_interactions_collection.drop()

# Insert sample customers
customers = [
    {"gender": "Male", "prior_purchases": 5},
    {"gender": "Female", "prior_purchases": 2},
]

customer_ids = customers_collection.insert_many(customers).inserted_ids

# Insert sample shipments
shipments = [
    {
        "warehouse_block": "A1",
        "mode_of_shipment": "Air",
        "weight_in_gms": 2000.5,
        "cost_of_the_product": 150.75,
        "discount_offered": 10.0,
    },
    {
        "warehouse_block": "B2",
        "mode_of_shipment": "Sea",
        "weight_in_gms": 5000.0,
        "cost_of_the_product": 300.00,
        "discount_offered": 20.0,
    },
]

shipments_collection.insert_many(shipments)

# Insert sample customer interactions
customer_interactions = [
    {
        "customer_id": customer_ids[0],  # Reference to the first customer
        "customer_care_calls": 3,
        "customer_rating": 4.5,
        "reached_on_time": True,
    },
    {
        "customer_id": customer_ids[1],  # Reference to the second customer
        "customer_care_calls": 1,
        "customer_rating": 3.0,
        "reached_on_time": False,
    },
]

customer_interactions_collection.insert_many(customer_interactions)

# Print confirmation
print("Data inserted successfully!")
print("Customers:", list(customers_collection.find()))
print("Shipments:", list(shipments_collection.find()))
print("Customer Interactions:", list(customer_interactions_collection.find()))

# Close the connection
client.close()
