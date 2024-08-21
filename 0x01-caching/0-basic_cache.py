#!/usr/bin/env python3
"""
   Create a class BasicCache
   that inherits from BaseCaching
   and is a caching system:

   You must use self.cache_data -
   dictionary from the parent
   class BaseCaching This caching
   system doesn’t have limit
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
       Must assign to the dictionary
       self.cache_data the item
       value for the key key.
    """

    def put(self, key, item):
        """
            Must assign to the dictionary
            self.cache_data the item
            value for the key key.
        """
        if key and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
           Must return the value in
           self.cache_data linked to key
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key, None)
