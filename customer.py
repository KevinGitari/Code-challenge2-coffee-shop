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

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        order = order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.is_valid_coffee(coffee):
            return None

        customer_spending = {}
        for customer in cls.customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > 0:
                customer_spending[customer] = total_spent

        if customer_spending:
            return max(customer_spending, key=customer_spending.get)
        return None
    
