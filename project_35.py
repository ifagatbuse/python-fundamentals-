# Project 35: Shopping Cart
# Topic: OOP-based shopping cart system

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, price, quantity=1):
        if product in self.items:
            self.items[product]["quantity"] += quantity
        else:
            self.items[product] = {"price": price, "quantity": quantity}
        print(f"Added {quantity} x {product}")

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
            print(f"{product} removed from cart.")
        else:
            print("Item not found in cart.")

    def view_cart(self):
        print("\n--- Your Cart ---")
        total = 0
        for product, details in self.items.items():
            subtotal = details["price"] * details["quantity"]
            total += subtotal
            print(f"{product}: {details['quantity']} x {details['price']}$ = {subtotal}$")
        print("Total:", total, "$")

cart = ShoppingCart()
cart.add_item("Book", 10, 2)
cart.add_item("Pen", 2, 5)
cart.view_cart()
cart.remove_item("Pen")
cart.view_cart()
