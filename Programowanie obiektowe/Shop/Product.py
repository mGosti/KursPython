
from dataclasses import dataclass

@dataclass
class Product:
    # def __init__(self,name, category, unit_price, identifier=000):
    #     self.unit_price = unit_price
    #     self.category = category
    #     self.name = name
    #     self.identifier = identifier

    name: str
    category: str
    unit_price: float
    identifier: int

    def __str__(self):
        return f"Produkt: {self.name}, Kategoria: {self.category}, Cena jednostkowa: {self.unit_price} zł, ID: {self.identifier}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
             return NotImplemented
        if self.name == other.name and self.category == other.category and self.unit_price == other.unit_price:
            return True
        else:
            return False


@dataclass
class ProductWithExpiryDate(Product):
    # def __init__(self, name, category, unit_price, production_year, valid_for):
    #     super().__init__(name, category, unit_price)
    #     self.production_year = production_year
    #     self.valid_for = valid_for

    production_year: int
    valid_for: int


    def does_expire(self, actual_year):

        if self.production_year + self.valid_for >= actual_year:
            print("Produkt zdatny do spożycia")
            return True
        else:
            print("Produkt niezdatny do spożycia!!!")
            return False







