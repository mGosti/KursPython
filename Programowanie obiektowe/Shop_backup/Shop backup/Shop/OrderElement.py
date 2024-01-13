from Product import Product
from TaxCalculator import TaxCalculator

class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


    def __str__(self):
        return f"Produkt: {self.product.name}; Kategoria: {self.product.category};    Ilość: {self.quantity}; Łączna cena: {self.total_price()}; Podatek: {self.tax()}"

    def total_price(self):
        total_price = self.product.unit_price * self.quantity
        return total_price

    def tax(self):
        tax = TaxCalculator.tax_amount(self)
        return tax

    def __eq__(self, other):
        if self.__class__ != other.__class__:
             return NotImplemented
        if self.product == other.product and self.quantity == other.quantity:
            return True
        else:
            return False
