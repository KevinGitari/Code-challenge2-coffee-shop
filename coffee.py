class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

    def add_order(self, order):
        if isinstance(order, Order):
            self._orders.append(order)

    @staticmethod
    def is_valid_coffee(coffee):
        return isinstance(coffee, Coffee)


class Order:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

coffee = Coffee("Latte")

order1 = Order("John", 5.0)
order2 = Order("Jane", 4.5)
order3 = Order("John", 5.5)

coffee.add_order(order1)
coffee.add_order(order2)
coffee.add_order(order3)

print("Coffee Name:", coffee.name)
print("Orders:", coffee.num_orders())
print("Customers:", coffee.customers())
print("Average Price:", coffee.average_price())