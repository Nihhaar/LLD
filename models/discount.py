class Discount:
    def __init__(
        self,
        discount_id,
        discount_in_percent,
        max_discount,
    ) -> None:
        self.__discount_id = discount_id
        self.discount_in_percent = discount_in_percent
        self.max_discount = max_discount
