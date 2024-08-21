#!/usr/bin/env python3
""""""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """"""

    def __init__(self):
        """"""

        super().__init__()

    def put(self, key, item):
        """"""

        if key or item is not None:

