from fastapi import FastAPI, HTTPException
from models import Customer, Product, Order, Shipment
from data import customers_collection, products_collection, orders_collection, shipments_collection
from bson import ObjectId
from pymongo import DESCENDING

app = FastAPI()

# Helper function to serialize MongoDB document
def serialize_doc(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

# CRUD for Customers
@app.post("/customers/")
async def create_customer(customer: Customer):
    customer_dict = customer.dict()
    customer_dict["_id"] = str(ObjectId())  # Generate a new ObjectId
    result = customers_collection.insert_one(customer_dict)
    return {"inserted_id": str(result.inserted_id)}

@app.get("/customers/{customer_id}")
async def read_customer(customer_id: str):
    customer = customers_collection.find_one({"_id": customer_id})
    if customer:
        return serialize_doc(customer)
    raise HTTPException(status_code=404, detail="Customer not found")

@app.put("/customers/{customer_id}")
async def update_customer(customer_id: str, customer: Customer):
    result = customers_collection.update_one({"_id": customer_id}, {"$set": customer.dict()})
    if result.modified_count:
        return {"message": "Customer updated successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")

@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: str):
    result = customers_collection.delete_one({"_id": customer_id})
    if result.deleted_count:
        return {"message": "Customer deleted successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")

# Endpoint to get the latest customer entry
@app.get("/customers/latest")
async def get_latest_customer():
    latest_customer = customers_collection.find().sort("_id", DESCENDING).limit(1)
    latest_customer = list(latest_customer)
    if latest_customer:
        return serialize_doc(latest_customer[0])
    raise HTTPException(status_code=404, detail="No customer data found")

# CRUD for Products
@app.post("/products/")
async def create_product(product: Product):
    product_dict = product.dict()
    product_dict["_id"] = str(ObjectId())
    result = products_collection.insert_one(product_dict)
    return {"inserted_id": str(result.inserted_id)}

@app.get("/products/{product_id}")
async def read_product(product_id: str):
    product = products_collection.find_one({"_id": product_id})
    if product:
        return serialize_doc(product)
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}")
async def update_product(product_id: str, product: Product):
    result = products_collection.update_one({"_id": product_id}, {"$set": product.dict()})
    if result.modified_count:
        return {"message": "Product updated successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
async def delete_product(product_id: str):
    result = products_collection.delete_one({"_id": product_id})
    if result.deleted_count:
        return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

# Endpoint to get the latest product entry
@app.get("/products/latest")
async def get_latest_product():
    latest_product = products_collection.find().sort("_id", DESCENDING).limit(1)
    latest_product = list(latest_product)
    if latest_product:
        return serialize_doc(latest_product[0])
    raise HTTPException(status_code=404, detail="No product data found")

# CRUD for Orders
@app.post("/orders/")
async def create_order(order: Order):
    order_dict = order.dict()
    order_dict["_id"] = str(ObjectId())
    result = orders_collection.insert_one(order_dict)
    return {"inserted_id": str(result.inserted_id)}

@app.get("/orders/{order_id}")
async def read_order(order_id: str):
    order = orders_collection.find_one({"_id": order_id})
    if order:
        return serialize_doc(order)
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{order_id}")
async def update_order(order_id: str, order: Order):
    result = orders_collection.update_one({"_id": order_id}, {"$set": order.dict()})
    if result.modified_count:
        return {"message": "Order updated successfully"}
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{order_id}")
async def delete_order(order_id: str):
    result = orders_collection.delete_one({"_id": order_id})
    if result.deleted_count:
        return {"message": "Order deleted successfully"}
    raise HTTPException(status_code=404, detail="Order not found")

# Endpoint to get the latest order entry
@app.get("/orders/latest")
async def get_latest_order():
    latest_order = orders_collection.find().sort("_id", DESCENDING).limit(1)
    latest_order = list(latest_order)
    if latest_order:
        return serialize_doc(latest_order[0])
    raise HTTPException(status_code=404, detail="No order data found")

# CRUD for Shipments
@app.post("/shipments/")
async def create_shipment(shipment: Shipment):
    shipment_dict = shipment.dict()
    shipment_dict["_id"] = str(ObjectId())
    result = shipments_collection.insert_one(shipment_dict)
    return {"inserted_id": str(result.inserted_id)}

@app.get("/shipments/{shipment_id}")
async def read_shipment(shipment_id: str):
    shipment = shipments_collection.find_one({"_id": shipment_id})
    if shipment:
        return serialize_doc(shipment)
    raise HTTPException(status_code=404, detail="Shipment not found")

@app.put("/shipments/{shipment_id}")
async def update_shipment(shipment_id: str, shipment: Shipment):
    result = shipments_collection.update_one({"_id": shipment_id}, {"$set": shipment.dict()})
    if result.modified_count:
        return {"message": "Shipment updated successfully"}
    raise HTTPException(status_code=404, detail="Shipment not found")

@app.delete("/shipments/{shipment_id}")
async def delete_shipment(shipment_id: str):
    result = shipments_collection.delete_one({"_id": shipment_id})
    if result.deleted_count:
        return {"message": "Shipment deleted successfully"}
    raise HTTPException(status_code=404, detail="Shipment not found")

# Endpoint to get the latest shipment entry
@app.get("/shipments/latest")
async def get_latest_shipment():
    latest_shipment = shipments_collection.find().sort("_id", DESCENDING).limit(1)
    latest_shipment = list(latest_shipment)
    if latest_shipment:
        return serialize_doc(latest_shipment[0])
    raise HTTPException(status_code=404, detail="No shipment data found")
