#!/usr/bin/env python3
"""Discard the least frequency used item (LFU algorithm)"""
from collections import defaultdict, OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
        Use self.cache_data - dictionary
        from the parent class BaseCaching
    """

    def __init__(self):
        """Initialize and overload the parent class"""

        super().__init__()
        self.d_count = defaultdict(int)
        self.usage = OrderedDict()

    def put(self, key, item):
        """Add an item to dictionary"""

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.d_count[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_use = min(self.d_count.values())
                d_key = [k for k, v in self.d_count.items() if v == min_use]
                if len(d_key) == 1:
                    k_key = d_key[0]
                else:
                    for k in self.usage:
                        if k in d_key:
                            k_key = k
                            break
                del self.cache_data[k_key]
                del self.d_count[k_key]
                self.usage.pop(k_key, None)
                print(f"DISCARD: {k_key}")
        self.cache_data[key] = item
        self.d_count[key] = 1

        self.usage.pop(key, None)
        self.usage[key] = None

    def get(self, key):
        """Get item value by key"""

        if key is None or key not in self.cache_data:
            return None

        self.d_count[key] += 1
        self.usage.pop(key, None)
        self.usage.[key] = None
        return self.cache_data.get(key)
