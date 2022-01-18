from services.order_service import OrderService
from .cart import Cart


class Customer:
    def __init__(
        self,
        customer_id,
        customer_name,
        mobile_number,
        location,
    ) -> None:
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__mobile_number = mobile_number
        self.__cart = Cart()
        self.__order = None
        self.__location = location

    @property
    def location(self):
        return self.__location

    @property
    def cart(self):
        return self.__cart

    def place_order(self):
        self.__order = OrderService.place_order(self, self.__cart)
        return self.__order

    def track_order(self):
        OrderService.track_order(self, self.__order)
