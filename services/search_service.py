from .database import get_entry


class SearchService:

    @staticmethod
    def get_all_restaurants():
        return get_entry("Restaurant")
