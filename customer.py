class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @classmethod
    def create_order(cls, customer, coffee, price):
        return cls(customer, coffee, price)

class Customer:
    customers = []

    def __init__(self, name):
        self._name = name
        self._orders = []
        Customer.customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def get_orders(self):
        return self._orders

    def get_coffees(self):
        return list(set(order.coffee for order in self._orders if order.coffee is not None))

    def create_order(self, coffee, price):
        order = Order.create_order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for customer in cls.customers:
            total_spent = sum(order.price for order in customer.get_orders() if order.coffee == coffee)
            if total_spent > 0:
                customer_spending[customer] = total_spent

        if customer_spending:
            return max(customer_spending, key=customer_spending.get)
        return None


customer1 = Customer("Kevin")
customer2 = Customer("Gitari")

customer1.create_order("Latte", 5)
customer1.create_order("Latte", 5)
customer1.create_order("Cappuccino", 4)

customer2.create_order("Latte", 3)
customer2.create_order("Cappuccino", 4)
customer2.create_order("Cappuccino", 4)

print(Customer.most_aficionado("Latte").name) 
print(Customer.most_aficionado("Cappuccino").name) 