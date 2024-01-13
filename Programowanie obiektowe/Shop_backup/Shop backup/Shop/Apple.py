class Apple:
    def __init__(self, species, size, unit_price):
        self.species = species
        self.size = size
        self.unit_price = unit_price

    def total_price(self, number_of_kgs):
        total_price = self.unit_price * number_of_kgs
        print(f"Łączna cena = {total_price}")

    def __repr__(self):
        return f"<Apple - rodzaj: {self.species}, rozmair: {self.size}, cena jednostkowa: {self.unit_price} "