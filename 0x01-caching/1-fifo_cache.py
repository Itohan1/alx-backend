#!/usr/bin/env python3
""""""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """"""

    def __init__(self):
        """Overloading"""

        super().__init__()

    def put(self, key, item):
        """Updating the dictionary"""

        if key and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key, value = list(self.cache_data.items())[0]
                print(f"DISCARD: {key}")
                del self.cache_data[next(iter(self.cache_data))]

    def get(self, key):
        """Returns value linked to key"""

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.value()
