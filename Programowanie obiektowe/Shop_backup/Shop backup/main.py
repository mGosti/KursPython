from typing import List

from Shop.Apple import Apple
from Shop.Potato import Potato
from Shop.Order import Order
from Shop.Product import Product, Product_with_expiry_date
from Shop.OrderElement import OrderElement
import random
from Discounts import standard_policy, christmas_discount, loyal_customer
from DataGenerator import generate_order_elements



def run_example():
    produkt = Product_with_expiry_date("Prod", "Kat", 2)





if __name__ == '__main__':
    run_example()