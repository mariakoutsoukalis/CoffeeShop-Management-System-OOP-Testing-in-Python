class Pizza:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.customers = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        NAME_IS_STR = isinstance(name, str)
        NAME_EXISTS = (not hasattr(self, "name"))
        if NAME_IS_STR and NAME_EXISTS:
            self._name = name
        else:
            raise Exception("`Pizza.name` already exists!")

    def orders(self, new_order=None):
        from classes.order import Order
        ORDER_ALREADY_CREATED = (new_order is not None)
        ORDER_TYPE_IS_VALID = isinstance(new_order, Order)
        if ORDER_ALREADY_CREATED and ORDER_TYPE_IS_VALID:
            self._orders.append(new_order)
        return self._orders

    def customers(self, new_customer=None):
        from classes.customer import Customer
        CUSTOMER_IS_UNIQUE = (new_customer not in self._customers)
        CUSTOMER_TYPE_IS_VALID = isinstance(new_customer, Customer)
        if CUSTOMER_IS_UNIQUE and CUSTOMER_TYPE_IS_VALID:
            self._customers.append(new_customer)
        return self._customers

    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        total_price = 0
        for order in self._orders:
            total_price += order.price
        return total_price / self.num_orders()