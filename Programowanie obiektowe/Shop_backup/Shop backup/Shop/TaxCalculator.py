

class TaxCalculator:

    FRUIT_AND_VEGETABLES_TAX_RATE = 0.05
    FOOD_TAX_RATE = 0.08
    OTHERS_TAX_RATE = 0.2

    @staticmethod
    def tax_amount(order_element):
        if order_element.product.category == "Owoce i warzywa":
            tax_amount = round(order_element.total_price() * TaxCalculator.FRUIT_AND_VEGETABLES_TAX_RATE,2)
        elif order_element.product.category == "Jedzenie":
            tax_amount = round(order_element.total_price() * TaxCalculator.FOOD_TAX_RATE,2)
        else:
            tax_amount = round(order_element.total_price() * TaxCalculator.OTHERS_TAX_RATE,2)
        return tax_amount
