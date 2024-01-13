import random
from random import randint

from OrderElement import OrderElement
from Order import Order
from Product import Product


def generate_order_elements(number_of_products=None, discount_policy=None):
    list_of_order_elements = []

    MIN_UNIT_PRICE = 1
    MAX_UNIT_PRICE = 5
    MIN_QTY = 1
    MAX_QTY = 4

    if number_of_products == None:
        number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENTS)

    for i in range(0, number_of_products):
        product = Product(f"Produkt-{i}", f"Kategoria-{random.randint(1, Order.MAX_ORDER_ELEMENTS)}",\
                          random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE), random.randint(100,999))
        quantity = random.randint(MIN_QTY, MAX_QTY)

        order_element = OrderElement(product, quantity)
        list_of_order_elements.append(order_element)
    return list_of_order_elements

    # for i in range(0, number_of_products):
    #     if i == 1:
    #         product = Product(f"Produkt-{i}", f"Owoce i warzywa", round((i + 2) * 0.895, 2))
    #     elif i == 3:
    #         product = Product(f"Produkt-{i}", f"Jedzenie", round((i + 2) * 0.895, 2))
    #     else:
    #         product = Product(f"Produkt-{i}", f"Kategoria-{i}", round((i + 2) * 0.895, 2))
    #     quantity = (i + 1) * 2
    #     order_element = OrderElement(product, quantity)
    #     list_of_order_elements.append(order_element)

    # return Order("Maciej", "Gostylla", list_of_order_elements, discount_policy)