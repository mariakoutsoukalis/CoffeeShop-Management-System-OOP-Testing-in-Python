class Coffee:
    def __init__(self, name):
        self.name = name
        self.transaction = []
        self.customers = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        name_is_str = isinstance(name, str)
        name_exists = (not hasattr(self, "name"))
        if name_is_str and name_exists:
            self._name = name
        else:
            raise Exception ("Item Already Created")
        

    def access_current_transactions(self, new_transaction=None):
        from classes.transaction import Transaction
        transaction_already_exists = (new_transaction is not None)
        transaction_valid = isinstance(new_transaction, Transaction)
        if transaction_already_exists and transaction_valid :
            self.transaction.append(new_transaction)
        return self.transaction
        

    def access_current_customers(self, new_customer=None):
        from classes.customer import Customer
        customer_unique = (new_customer not in self.customers)
        customer_valid = isinstance(new_customer, Customer)
        if customer_unique and customer_valid:
            self.customers.append(new_customer)
        return self.customers

    def calculate_total_number_of_transactions(self):
        return len(self.transaction)
    
    def calculate_average_price_across_all_transactions(self):
        total_price = 0
        for transaction in self.transaction:
            total_price += transaction.price
        return total_price / self.calculate_total_number_of_transactions()