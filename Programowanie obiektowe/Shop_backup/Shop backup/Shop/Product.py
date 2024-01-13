class Product:
    def __init__(self,name, category, unit_price):
        self.unit_price = unit_price
        self.category = category
        self.name = name

    def __str__(self):
        return f"Produkt: {self.name}, Kategoria: {self.category}, Cena jednostkowa: {self.unit_price} zł"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
             return NotImplemented
        if self.name == other.name and self.category == other.category and self.unit_price == other.unit_price:
            return True
        else:
            return False






