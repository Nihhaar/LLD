from models.delivery_agent import DeliveryAgent
from models.order import Order
from typing import Tuple
from .database import get_entry


class DeliveryService:

    @staticmethod
    def calculate_distance(loc1, loc2):
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

    @staticmethod
    def assign_delivery_agent(
        order: Order,
        restaurant_location: Tuple[float, float]
    ):
        min_distance = 1000000
        delivery_agent: DeliveryAgent = None
        for agent in get_entry("DeliveryAgent"):
            if agent.is_online:
                distance = DeliveryService.calculate_distance(
                            agent.location,
                            restaurant_location
                        )
                if min_distance > distance:
                    min_distance = distance
                    delivery_agent = agent

        delivery_agent.accept_order(order)
