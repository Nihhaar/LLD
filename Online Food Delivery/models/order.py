from enum import Enum
from typing import List

from .restaurant import MenuItem, Restaurant


class OrderStatus(Enum):
    PENDING = 0
    RESTAURANT_ACCEPTED = 1
    DELIVERY_AGENT_ACCEPTED = 2
    DELIVERED = 3


class Order:
    def __init__(
        self,
        order_id: int,
        customer,
        order_restaurant: Restaurant,
        order_menu: List[MenuItem],
    ) -> None:
        self.__order_id = order_id
        self.__customer = customer
        self.__order_restaurant = order_restaurant
        self.__order_menu = order_menu
        self.__order_status = OrderStatus.PENDING
        self.__agent = None

    @property
    def id(self):
        return self.__order_id

    @property
    def status(self):
        return self.__order_status

    def update_status(self, status: OrderStatus):
        self.__order_status = status

    def update_agent(self, agent):
        self.__agent = agent

    @property
    def agent(self):
        return self.__agent
