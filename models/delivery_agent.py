from .order import Order, OrderStatus


class DeliveryAgent:
    def __init__(
        self,
        delivery_agent_id,
        delivery_agent_name,
        mobile_number,
    ) -> None:
        self.__delivery_agent_id = delivery_agent_id
        self.__delivery_agent_name = delivery_agent_name
        self.__mobile_number = mobile_number
        self.__is_online = False
        self.__location = None
        self.__amount = 0
        self.__current_orders = {}
        self.__historic_orders = {}

    def come_online(self, location):
        self.__is_online = True
        self.__location = location

    @property
    def id(self):
        return self.__delivery_agent_id

    @property
    def historic_orders(self):
        return self.__historic_orders

    @property
    def is_online(self):
        return self.__is_online

    @property
    def location(self):
        return self.__location

    def accept_order(self, order: Order):
        print(f"Order {order.id} is assigned to delivery agent {self.id}")
        self.__current_orders[order.id] = order
        order.update_status(OrderStatus.DELIVERY_AGENT_ACCEPTED)
        order.update_agent(self)

    def deliver_order(self, order: Order):
        self.__current_orders[order.id].update_status(OrderStatus.DELIVERED)
        delivered_order = self.__current_orders.pop(order.id)
        self.__historic_orders[order.id] = delivered_order
