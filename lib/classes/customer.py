class Customer:    
    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.coffee = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        name_is_str = isinstance(name, str)
        name_in_charc_limit = (1 <= len(name) <= 15)
        if name_is_str and name_in_charc_limit:
            self._name = name
        else:
            raise Exception("Invalid")

    def access_current_transactions(self, new_transaction=None):
        from classes.transaction import Transaction
        transaction_already_exists = (new_transaction is not None)
        transaction_valid = isinstance(new_transaction, Transaction)
        if transaction_already_exists and transaction_valid :
            self.transactions.append(new_transaction)
        return self.transactions

    def access_current_coffees(self, new_coffee=None, ):
        from classes.coffee import Coffee
        coffee_unique = (new_coffee not in self.coffee)
        coffee_valid = isinstance(new_coffee, Coffee)
        if coffee_unique and coffee_valid:
            self.coffee.append(new_coffee)
        return self.coffee

    def place_order(self, name_of_coffee, price):
        from classes.coffee import Coffee
        from classes.transaction import Transaction
        return Transaction(self, Coffee(name_of_coffee), price)

    def calculate_total_money_spent(self):
        return sum(transaction.price for transaction in self.transactions)
    
    def retrieve_coffees_within_price_range(self, min_price=0, max_price=999):
        filtered_transactions = list(filter(lambda transaction: min_price <= transaction.price <= max_price, self.transactions))
        return [filtered_transaction.coffee for filtered_transaction in filtered_transactions]
        #return list(coffee for coffee in self.transactions if min_price <= coffee.price <= max_price)