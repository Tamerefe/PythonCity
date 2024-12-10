def totalcost(price):
    def applytax(tax):
        def applydiscount(discount):
            return price + price*tax - price*discount
        return applydiscount
    return applytax

price = 100
tax = 0.05
discount = 0.1

print(totalcost(price)(tax)(discount))