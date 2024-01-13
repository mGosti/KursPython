class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price

class PercentageDiscount(DiscountPolicy):

    def __init__(self, discount_percent):
        self.discount_percent = discount_percent

    def apply_discount(self, total_price):
        return total_price * (100 - self.discount_percent) / 100


class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, total_price):

        if self.discount_amount < total_price:
            return total_price - self.discount_amount
        return 0



