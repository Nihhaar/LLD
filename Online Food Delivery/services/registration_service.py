from .database import add_entry
from models.restaurant import Restaurant
from models.delivery_agent import DeliveryAgent
from models.customer import Customer


class RegistrationService:

    @staticmethod
    def register_restaurant(restaurant: Restaurant):
        add_entry("Restaurant", restaurant)

    @staticmethod
    def register_delivery_agent(delivery_agent: DeliveryAgent):
        add_entry("DeliveryAgent", delivery_agent)

    @staticmethod
    def register_customer(customer: Customer):
        add_entry("Customer", customer)
