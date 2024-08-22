#!/usr/bin/env python3
"""
     a class LRUCache that inherits
     from BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """All the LRUCache methods"""

    def __init__(self):
        """
            self.cache_data - dictionary from
            the parent class BaseCaching
        """

        super().__init__()
        self.order = []

    def put(self, key, item):
        """
            Must assign to the dictionary
            self.cache_data the item
            value for the key key
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            d_key = self.order.pop(0)
            del self.cache_data[d_key]
            print(f"DISCARD: {d_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
            Must return the value in
            self.cache_data linked to key
        """

        if key is None or key not in self.cache_data:

            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data.get(key)
