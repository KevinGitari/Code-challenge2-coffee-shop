## Coffee Shop Project

Welcome to the Coffee Shop Project! This project models a simple coffee shop system using Python's object-oriented programming principles. It includes classes for `Customer`, `Coffee`, and `Order`, and demonstrates how to use these classes together.

## Project Overview

- **Customer**: Represents a customer who can place orders.
- **Coffee**: Represents different types of coffee available.
- **Order**: Represents an order that links a customer to a coffee with a specified price.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

Clone this repository to your local machine using:
```bash
git clone https://github.com/KevinGitari/code-challenge2-coffee-shop
```

### 2. Navigate to the Project Folder

Change into the project directory:
```bash
cd coffee_shop
```

## How to Use

### Creating Instances

**1. Create a Coffee Instance**

- **Name**: Coffee names must be at least 3 characters long and cannot be changed after creation.

**2. Create a Customer Instance**

- **Name**: Customer names must be between 1 and 15 characters long and can be changed after creation.

**3. Create an Order**


- **Price**: Order prices must be between 1.0 and 10.0, inclusive.

### Callback Function

You can set a callback function that will be triggered when a new order is created. This function will be called with the new order as an argument.

**1. Define a Callback Function**

**2. Set the Callback Function for a Customer**

**3. Create an Order and Trigger the Callback**

### Using Methods

**1. Get a Customer's Order**

**2. Get the Customer's Ordered Coffees**

**3. Get the Coffee's Orders**

**4. Get the Coffee's Customers**

**5. Get the Number of Orders for a Coffee**

**6. Get the Average Price of Orders for a Coffee**

## Additional Notes

- **Error Handling**: The code includes error handling to ensure that names and prices adhere to the specified constraints.
- **Data Integrity**: The system maintains relationships between customers, coffees, and orders, ensuring data consistency.
