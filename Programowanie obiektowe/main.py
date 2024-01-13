from typing import List

from Shop.Apple import Apple
from Shop.Potato import Potato
from Shop.Order import Order, ExpressOrder
from Shop.Product import Product, ProductWithExpiryDate
from Shop.OrderElement import OrderElement
import random
from Discounts import standard_policy, christmas_discount, loyal_customer
from DataGenerator import generate_order_elements
from DiscountPolicy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount
from collections import namedtuple


def run_example():



    ele = generate_order_elements(6)
    zam = Order("m", "g", ele)
    print(zam)





if __name__ == '__main__':
    run_example()