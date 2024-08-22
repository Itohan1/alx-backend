#!/usr/bin/env python
"""
   Create a class LIFOCache that
   inherits from BaseCaching
   and is a caching system:

   You must use self.cache_data -
   dictionary from the parent class BaseCaching

   You can overload def __init__(self):
   but don’t forget to call the
   parent init: super().__init__()
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
        a class LIFOCache that inherits
        from BaseCaching and is a caching system
    """

    def __init__(self):
        """Modifying the parent class __init__ method"""

        super().__init__()
        self.order = []

    def put(self, key, item):
        """
            Must assign to the dictionary
           self.cache_data the item
           value for the key key.

           If key or item is None, this
           method should not do anything.
           If the number of items in self.cache_data
           is higher that BaseCaching.MAX_ITEMS:

           you must discard the last item
           put in cache (LIFO algorithm)

           you must print DISCARD: with the
           key discarded and following by a new line
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            d_key = self.order.pop()
            del self.cache_data[d_key]
            print(f"DISCARD: {d_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
            Must return the value in
            self.cache_data linked to key.

            If key is None or if the key
            doesn’t exist in self.cache_data, return None.
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
