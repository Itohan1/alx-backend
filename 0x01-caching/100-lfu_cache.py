#!/usr/bin/env python3
""""""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """"""

    def __init__(self):
        """"""

        super().__init__()
        self.d_count = []

    def put(self, key, item):
        """"""

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.d_count[key] += 1
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_use = min(self.d_count.values())

            d_key = [k for k, v in self.cache_id.items() if v == min_use]
            k_key = d_key[0]
            del self.cache_data[k_key]
            del self.d_count[k_key]
            print(f"DISCARD: {k_key}")
        self.cache_data[key] = item
        self.d_count[key] = 1

    def get(self, key):
        """"""

        if key is None or key not in self.cache_data:
            return None

        for i in self.order:
            for k, value in i.items():
                if key == i.keys():
                    self.order.remove(i)
                    i[key] = value + 1

        return self.cache_data.get(key)
