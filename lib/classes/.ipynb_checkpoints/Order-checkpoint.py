class Order:
    catalog = []

    def __init__(self, customer, pizza, price):
        self.customer = customer
        self.pizza = pizza
        self.price = price

        Order.catalog.append(self)

        pizza.orders(self)
        pizza.customers(customer)
        
        customer.orders(self)
        customer.pizzas(pizza)

    def __repr__(self):
        return f"{self.customer.name} ordered a {self.pizza.name}."

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        PRICE_IS_NUMERICAL = (type(price) in (int, float))
        PRICE_WITHIN_ACCEPTABLE_RANGE = (0.25 <= price <= 20)
        if PRICE_IS_NUMERICAL and PRICE_WITHIN_ACCEPTABLE_RANGE:
            self._price = price
        else:
            raise Exception("Unacceptable data format for `Order.price`!")

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        CUSTOMER_TYPE_IS_VALID = isinstance(customer, Customer)
        if CUSTOMER_TYPE_IS_VALID:
            self._customer = customer
        else:
            raise Exception("Unacceptable data type for `Order.customer`!")

    @property
    def pizza(self):
        return self._pizza

    @pizza.setter
    def pizza(self, pizza):
        PIZZA_TYPE_IS_VALID = isinstance(pizza, Pizza)
        if PIZZA_TYPE_IS_VALID:
            self._pizza = pizza
        else:
            raise Exception("Unacceptable data type for `Order.pizza`!")