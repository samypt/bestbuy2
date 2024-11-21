from product import Product

new_pr = Product("MacBook", price=1450, quantity=100)

print(new_pr)

new_pr.name = ""

print(new_pr)

print(new_pr.quantity)