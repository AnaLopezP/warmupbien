customer_basket_cost = 34
shipping_cost_per_kg = 1.2
customer_basket_weight = 44
if customer_basket_cost >= 100:
    print(str(customer_basket_cost) + "€")
else:
    shipping_cost = shipping_cost_per_kg * customer_basket_weight
    total_price = shipping_cost + customer_basket_cost
    print(str(total_price) + "€")
    