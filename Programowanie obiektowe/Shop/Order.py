import random
from Product import Product
from OrderElement import OrderElement
from Discounts import standard_policy, christmas_discount, loyal_customer
from DiscountPolicy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount

class Order:

    MAX_ORDER_ELEMENTS = 7

    def __init__(self, customer_name, customer_surname, order_elements=None, discount_policy=None):
        self.customer_surname = customer_surname
        self.customer_name = customer_name
        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ORDER_ELEMENTS:
            raise ValueError("Przekroczono maksymalną ilość elementów zamówienia")
        #     order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS]
        self._order_elements = order_elements

        if discount_policy == None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy
        self.total_price = self._calculate_total_price()

    def _calculate_total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.total_price()
        return self.discount_policy.apply_discount(total_price)

    def add_to_order(self, product, quantity):
        if len(self._order_elements) == Order.MAX_ORDER_ELEMENTS:
            print("Nie można dodać produktu, przekroczono maksymalną ilość")
        else:
            new_order_element = OrderElement(product, quantity)
            self._order_elements.append(new_order_element)
            self.total_price = self._calculate_total_price()

    def get_order_elements(self):
        return self._order_elements

    # @property
    # def total_price(self):
    #     total_price = 0
    #     for element in self._order_elements:
    #         total_price += element.total_price()
    #     return self.discount_policy(total_price)

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) <= Order.MAX_ORDER_ELEMENTS:
            self._order_elements = value
        else:
            self._order_elements = value[:Order.MAX_ORDER_ELEMENTS]

        self.total_price = self._calculate_total_price()

    def __str__(self):

        mark_line = ("=" * 50)
        order_details = f"Zamówienie złożone przez: {self.customer_name} {self.customer_surname}"
        products_list = ("Lista produktów:\n")
        for element in self._order_elements:
            products_list += f"{element}\n"
        total_order_price = (f"Łączna kwota zamówienia: {self.total_price:2f}")

        result = "\n".join([mark_line, order_details, mark_line, products_list, mark_line, total_order_price])
        return result

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
             return NotImplemented
        if self.customer_name != other.customer_name or self.customer_surname != other.customer_surname:
            return False
        if len(self._order_elements) != len(other.order_elements):
            return False
        for order_element in self._order_elements:
            if order_element not in other.order_elements:
                return False

        return True

    # @classmethod
    # def sample_order(cls, number_of_products, discount_policy=None):
    #     list_of_order_elements = []
    #     # number_of_products = random.randint(1,11)
    #     # number_of_products = int(input("Podaj liczbę produktów"))
    #
    #
    #
    #     for i in range(0, number_of_products):
    #         if i == 1:
    #             product = Product(f"Produkt-{i}", f"Owoce i warzywa", round((i + 2) * 0.895, 2))
    #         elif i == 3:
    #             product = Product(f"Produkt-{i}", f"Jedzenie", round((i + 2) * 0.895, 2))
    #         else:
    #             product = Product(f"Produkt-{i}", f"Kategoria-{i}", round((i + 2) * 0.895, 2))
    #         quantity = (i + 1) * 2
    #         order_element = OrderElement(product, quantity)
    #         list_of_order_elements.append(order_element)
    #
    #
    #     return Order("Maciej", "Gostylla", list_of_order_elements, discount_policy)

class ExpressOrder(Order):

    EXPRESS_DELIVERY_FEE = 10

    def __init__(self, customer_name, customer_surname, order_date, order_elements=None, discount_policy=None):
        super().__init__(customer_name, customer_surname, order_elements, discount_policy)
        self.order_date = order_date

    # @property
    # def _calculate_total_price(self):
    #     total_price = 0
    #     for element in self._order_elements:
    #         total_price += element.total_price()
    #     return self.discount_policy(total_price) + ExpressOrder.EXPRESS_DELIVERY_FEE

    def _calculate_total_price(self):
        total_price = super()._calculate_total_price() - ExpressOrder.EXPRESS_DELIVERY_FEE
        return total_price

    def __str__(self):

        mark_line = ("=" * 50)
        order_details = f"Zamówienie złożone przez: {self.customer_name} {self.customer_surname}"
        products_list = ("Lista produktów:\n")
        for element in self._order_elements:
            products_list += f"{element}\n"
        total_order_price = (f"Łączna kwota zamówienia: {self.total_price:2f}")
        express_order = (f"Zamówienie ekspresowe!!! Termin dostawy: {self.order_date}")

        result = "\n".join([express_order, mark_line, order_details, mark_line, products_list, mark_line, total_order_price])
        return result







