class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

class Order:
    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        coffee.add_order(self)
        customer.add_order(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

customer = Customer("John")
coffee = Coffee("Latte")
order = Order(customer, coffee, 5.0)

print(order.customer.name)
print(order.coffee.name)   
print(order.price)          




