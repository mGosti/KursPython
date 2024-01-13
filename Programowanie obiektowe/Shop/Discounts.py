def standard_policy(total_price):
    return total_price

def loyal_customer(total_price):
    return total_price * 0.95

def christmas_discount(total_price):
    if total_price > 100:
        return total_price - 20
    else:
        return total_price
