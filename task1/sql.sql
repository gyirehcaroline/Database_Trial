-- Creating the Customers table
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Gender VARCHAR(10),
    PriorPurchases INT,
    CustomerCareCalls INT,
    CustomerRating INT
);

-- Creating the Products table
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Cost DECIMAL(10, 2), 
    ProductImportance VARCHAR(20),
    WeightInGms INT
);

-- Creating the Orders table
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    DiscountOffered DECIMAL(5, 2),
    ProductID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Creating the Shipments table
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    WarehouseBlock VARCHAR(1),
    ModeOfShipment VARCHAR(20),
    ReachedOnTime BOOLEAN, 
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);