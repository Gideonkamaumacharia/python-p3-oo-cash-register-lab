#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self,title,price,quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price

