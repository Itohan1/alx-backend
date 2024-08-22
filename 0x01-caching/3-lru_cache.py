#!/usr/bin/env python3
""""""
BaseCaching = __import__("base_caching").BaseCaching

class LRUCache(BaseCaching):
    """"""

    def __init__(self):
        """"""

        super().__init__()
        self.order = []

    def put(self, key, item):
        """"""

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            d_key = self.order.pop(0)
            del self.cache_data[d_key]
            print(f"DISCARD: {d_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """"""

        if key is None or key not in self.cache_data:

            return None

        return self.cache_data.get(key)
