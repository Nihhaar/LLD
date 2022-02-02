from typing import Tuple

from .discount import Discount


class MenuItem:
    def __init__(
        self,
        item_id,
        item_name,
        price,
    ) -> None:
        self.__item_id = item_id
        self.__item_name = item_name
        self.__price = price

    @property
    def price(self):
        return self.__price

    def __repr__(self) -> str:
        return self.__item_name


class Restaurant:
    def __init__(
        self,
        restaurant_id: int,
        name: str,
        owner_id: int,
        location: Tuple[float, float]  # Latitude, Longitude
    ) -> None:
        self.__restaurant_id = restaurant_id
        self.__name = name
        self.__owner_id = owner_id
        self.__location = location
        self.__menu = []
        self.__discount = None

    def add_menu_item(
        self,
        item: MenuItem,
    ) -> None:
        self.__menu.append(item)

    def delete_menu_item(
        self,
        item: MenuItem
    ) -> None:
        if item.id not in [it.id for it in self.__menu]:
            raise ValueError("Item not present in menu!")
        self.__menu = [it for it in self.__menu if it.id != item.id]

    def add_discount(
        self,
        discount: Discount,
    ) -> None:
        self.__discount = discount

    @property
    def discount(self) -> Discount:
        return self.__discount

    @property
    def location(self) -> Tuple[float, float]:
        return self.__location

    def __repr__(self) -> str:
        return self.__name
