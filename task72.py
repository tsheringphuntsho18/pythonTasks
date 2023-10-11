#calculate discount
def calculate_discounted_price(orginal_price, discount_percent):
    discount_price = (orginal_price * discount_percent)/100
    discounted_price = orginal_price - discount_price
    return discounted_price

#apply discount
def apply_discount(orginal_price,discount_percent):
    discount_price = (orginal_price * discount_percent)/100
    discounted_price = orginal_price - discount_price
    return f"The discounted price is {discounted_price}"

#shopping cart
def shopping_cart(orginal_price,discount_percent):
    shopping = apply_discount(orginal_price,discount_percent)
    return shopping
result = shopping_cart(50,20)
print(result)
    