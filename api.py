from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://mongo:agKvmIMvyJiUFElCTdjQMUZqLVjzkklB@junction.proxy.rlwy.net:27999")
db = client["shipping_dataset"]

# Pydantic models
class Customer(BaseModel):
    gender: str
    prior_purchases: int

class Shipment(BaseModel):
    warehouse_block: str
    mode_of_shipment: str
    weight_in_gms: float
    cost_of_the_product: float
    discount_offered: float

class CustomerInteraction(BaseModel):
    customer_id: str
    customer_care_calls: int
    customer_rating: float
    reached_on_time: bool

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)}
    )

# Create Customer
@app.post("/customers/", response_model=str)
def create_customer(customer: Customer):
    try:
        result = db.customers.insert_one(customer.dict())
        return str(result.inserted_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create customer: {str(e)}")

# Read Customers
@app.get("/customers/", response_model=List[Customer])
def read_customers():
    try:
        customers = list(db.customers.find())
        return [Customer(gender=c["gender"], prior_purchases=c["prior_purchases"]) for c in customers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read customers: {str(e)}")

# Update Customer
@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(customer_id: str, customer: Customer):
    try:
        result = db.customers.update_one({"_id": ObjectId(customer_id)}, {"$set": customer.dict()})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update customer: {str(e)}")

# Delete Customer
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: str):
    try:
        result = db.customers.delete_one({"_id": ObjectId(customer_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Customer not found")
        return {"detail": "Customer deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete customer: {str(e)}")
