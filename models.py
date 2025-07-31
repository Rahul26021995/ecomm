class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Customer:
    def __init__(self, name, is_premium=False):
        self.name = name
        self.is_premium = is_premium

class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total = sum(p.price for p in items)
        self.discount = 0
        self.shipping_fee = 0
        self.final_total = self.total
