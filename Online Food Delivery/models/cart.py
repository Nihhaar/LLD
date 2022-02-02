class Cart:
    def __init__(self) -> None:
        self.restaurant = None
        self.cart = None

    def add_item(self, restaurant, item):
        if self.restaurant is None:
            self.restaurant = restaurant
            self.cart = [item]
        elif self.restaurant == restaurant:
            self.cart.append(item)
        else:
            print("Emptying your cart, since this is another restaurant...")
            self.restaurant = restaurant
            self.cart = [item]

    def delete_item(self, item):
        self.cart.remove(item)

    def show_cart(self):
        print(f"## Restaurant: {self.restaurant}")
        for it in self.cart:
            print(f"#### Item: {it}")

    def calculate_price(self):
        total_price = sum([it.price for it in self.cart])
        print(f"Total price before discount is {total_price}")
        total_price = total_price - min(
            self.restaurant.discount.discount_in_percent * total_price / 100,
            self.restaurant.discount.max_discount
        )
        print(f"Total price after discount is {total_price}")
