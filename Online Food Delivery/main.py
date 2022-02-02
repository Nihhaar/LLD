from models.customer import Customer
from models.discount import Discount
from models.restaurant import MenuItem, Restaurant
from models.delivery_agent import DeliveryAgent

from services.registration_service import RegistrationService
from services.search_service import SearchService


def main():
    # Register restaurants
    print("Registering restaurants...")
    restaurant1 = Restaurant(1, "R1", "O1", (93.5, 91.5))
    item1 = MenuItem(1, "I1", 250)
    restaurant1.add_menu_item(item1)
    RegistrationService.register_restaurant(restaurant1)

    restaurant2 = Restaurant(2, "R2", "O2", (54, 108))
    item2 = MenuItem(2, "I2", 21)
    item3 = MenuItem(3, "I3", 12.5)
    item4 = MenuItem(4, "I4", 220)
    restaurant2.add_menu_item(item2)
    restaurant2.add_menu_item(item3)
    restaurant2.add_menu_item(item4)
    RegistrationService.register_restaurant(restaurant2)
    print()

    # Add discounts
    print("Adding discounts...")
    discount1 = Discount(1, 10, 100)
    discount2 = Discount(2, 5, 10)
    restaurant1.add_discount(discount1)
    restaurant2.add_discount(discount2)
    print()

    # Register delivery agents
    print("Registering delivery agents...")
    delivery_agent1 = DeliveryAgent(1, "D1", "9123456789")
    delivery_agent2 = DeliveryAgent(2, "D2", "9123456000")
    RegistrationService.register_delivery_agent(delivery_agent1)
    RegistrationService.register_delivery_agent(delivery_agent2)
    print()

    # Register customers
    print("Registering customers...")
    customer1 = Customer(1, "Nihhaar", "9987392241", (95, 120))
    print()

    # Delivery agent online
    print("Delivery agents came online...")
    delivery_agent1.come_online((32.5, 44.5))
    delivery_agent2.come_online((64.5, 24.5))
    print()

    # Search restaurants
    print("Listing all restaurants...")
    print(SearchService.get_all_restaurants())
    print()

    # Add some items
    print("Adding items to cart...")
    customer1.cart.add_item(restaurant1, item1)
    customer1.cart.add_item(restaurant2, item3)
    customer1.cart.add_item(restaurant2, item4)
    print()

    # Show cart
    print("Cart contains...")
    customer1.cart.show_cart()
    print()

    # Cart price
    print("Calculating cart price...")
    customer1.cart.calculate_price()
    print()

    # Place order
    print("Placing order...")
    order = customer1.place_order()
    print()

    # Track order
    print("Tracking order...")
    customer1.track_order()
    print()

    # Deliver order
    print("Your order is delivered!")
    agent = order.agent
    agent.deliver_order(order)
    print()

    # Delivery agents historic orders
    print("You delivery agent has delivered these orders before...")
    print(agent.historic_orders)
    print()


if __name__ == "__main__":
    main()
