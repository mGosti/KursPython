from dataclasses import dataclass

@dataclass
class Potato:
    # def __init__(self, species, size, unit_price):
    #     self.species = species
    #     self.size = size
    #     self.unit_price = unit_price

    species: str
    size: str
    unit_price: float

    def total_price(self, number_of_kgs):
        total_price = self.unit_price * number_of_kgs
        print(f"Łączna cena = {total_price}")

    def __repr__(self):
        return f"<Potato - rodzaj: {self.species}, rozmair: {self.size}, cena jednostkowa: {self.unit_price} "