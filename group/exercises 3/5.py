class Cart:
    def __init__(self, product, amount):
            self.product = product
            self.amount = amount

    def add_product(self):
        print(f"Product '{self.product}' added to cart successfully")

    def total_price(self):
        print("The total price", self.amount)

cart = Cart("Mango", 3000)
cart.add_product()
cart.total_price()