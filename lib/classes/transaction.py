class Transaction:
    counter, catalog = 0, []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        coffee.access_current_transactions(self)
        coffee.access_current_customers(customer)

        customer.access_current_transactions(self)
        customer.access_current_coffees(coffee)


        Transaction.counter += 1
        Transaction.catalog.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        price_is_num = (type(price) in (int, float))
        price_in_range = (1 <= price <= 25)
        if price_is_num and price_in_range:
            self._price = price
        else:
            raise Exception("Invalid")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        customer_type_valid = isinstance(customer, Customer)
        if customer_type_valid:
            self._customer = customer
        else:
            raise Exception("Invalid")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        from classes.coffee import Coffee
        coffee_type_valid = isinstance(coffee, Coffee)
        if coffee_type_valid:
            self._coffee = coffee
        else:
            raise Exception("Invalid")



    def __repr__(self):
        return f"{self.customer.name} ordered a {self.coffee.name} for ${self.price}."