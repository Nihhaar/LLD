from models.cart import Cart
from models.order import Order, OrderStatus
from services.delivery_service import DeliveryService


class OrderService:

    @staticmethod
    def place_order(customer, cart: Cart):
        # Create order
        order = Order(1, customer, cart.restaurant, cart.cart)

        # Update order status
        order.update_status(OrderStatus.PENDING)

        # Redirect to payment service and update delivery amount as well
        pass

        # Assign delivery
        DeliveryService.assign_delivery_agent(order, cart.restaurant.location)
        return order

    def track_order(customer, order: Order):
        distance = DeliveryService.calculate_distance(
            customer.location,
            order.agent.location
        )

        print(f"Your order {order.id} is at a distance of {distance}")
        print(f"Your current order status is {order.status}")
